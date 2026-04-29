import os
import pdfplumber
from pathlib import Path

def extract_pdf_to_markdown(pdf_path, output_path):
    """提取PDF内容并保存为Markdown格式"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            content = []
            content.append(f"# {Path(pdf_path).stem.replace('.note', '')}\n\n")

            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    content.append(f"## Page {page_num}\n\n")
                    content.append(text)
                    content.append("\n\n---\n\n")

            markdown_content = "".join(content)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            return True, None
    except Exception as e:
        return False, str(e)

def process_pdf_files(source_dir, target_dir):
    """批量处理PDF文件"""
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    pdf_files = list(source_path.rglob("*.pdf"))
    total = len(pdf_files)

    print(f"Found {total} PDF files to process")

    success_count = 0
    error_files = []

    for i, pdf_file in enumerate(pdf_files, 1):
        # 计算相对路径
        rel_path = pdf_file.relative_to(source_path)

        # 转换文件名：xxx.note.pdf -> xxx.md
        new_filename = rel_path.stem.replace('.note', '') + '.md'

        # 构建输出路径
        output_file = target_path / "微信笔记" / rel_path.parent / new_filename

        print(f"[{i}/{total}] Processing: {rel_path}")

        success, error = extract_pdf_to_markdown(pdf_file, output_file)

        if success:
            success_count += 1
            print(f"  [OK] Saved to: {output_file.relative_to(target_path)}")
        else:
            error_files.append((str(rel_path), error))
            print(f"  [ERROR] {error}")

    print(f"\n{'='*50}")
    print(f"Processing complete!")
    print(f"Success: {success_count}/{total}")
    print(f"Errors: {len(error_files)}")

    if error_files:
        print(f"\nError files:")
        for file, err in error_files[:10]:  # 只显示前10个错误
            print(f"  - {file}: {err}")
        if len(error_files) > 10:
            print(f"  ... and {len(error_files) - 10} more")

if __name__ == "__main__":
    source_directory = r"D:\data\weixinobU7VjkCk_AmLlHIEyIma41A4cyw_2026-04-17_1776425101732"
    target_directory = r"D:\tool\obsidian"

    process_pdf_files(source_directory, target_directory)
