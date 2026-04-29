-- 可用功率详情表
CREATE TABLE IF NOT EXISTS "t_business_available_power_detail" (
    id VARCHAR(32) PRIMARY KEY,
    config_id BIGINT NOT NULL,
    "day" VARCHAR(10) NOT NULL,
    time_min VARCHAR(5) NOT NULL,
    is_limited BOOLEAN NOT NULL DEFAULT FALSE,
    actual_energy NUMERIC(15,4),
    available_energy NUMERIC(15,4),
    agc_target_time TIMESTAMP,
    agc_target_value NUMERIC(10,2),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX IF NOT EXISTS idx_config_day ON "t_business_available_power_detail"(config_id, "day");

-- 添加表注释
COMMENT ON TABLE "t_business_available_power_detail" IS '可用功率详情表 - 每分钟一条记录';
COMMENT ON COLUMN "t_business_available_power_detail".id IS '主键ID（随机字符串）';
COMMENT ON COLUMN "t_business_available_power_detail".config_id IS '配置ID';
COMMENT ON COLUMN "t_business_available_power_detail"."day" IS '日期(yyyy-MM-dd)';
COMMENT ON COLUMN "t_business_available_power_detail".time_min IS '时间(HH:mm)';
COMMENT ON COLUMN "t_business_available_power_detail".is_limited IS '是否限电';
COMMENT ON COLUMN "t_business_available_power_detail".actual_energy IS '实际电量(KWh)';
COMMENT ON COLUMN "t_business_available_power_detail".available_energy IS '可用电量(KWh)';
COMMENT ON COLUMN "t_business_available_power_detail".agc_target_time IS 'AGC指令下达时间（限电时）';
COMMENT ON COLUMN "t_business_available_power_detail".agc_target_value IS 'AGC指令值(MW)（限电时）';
COMMENT ON COLUMN "t_business_available_power_detail".create_time IS '创建时间';
