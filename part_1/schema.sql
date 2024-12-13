-- schema diagram https://dbdiagram.io/d/schema_diagram-675bfd2fe763df1f00d65123

CREATE TABLE publisher_performance_reports (
    report_id SERIAL PRIMARY KEY,
    publisher_id INT,
    advertiser_id INT,
    region_id INT,
    currency_id INT,
    impressions INT,
    clicks INT,
    pending_count INT,
    pending_value DECIMAL(12,2),
    pending_commission DECIMAL(12,2),
    confirmed_count INT,
    confirmed_value DECIMAL(12,2),
    confirmed_commission DECIMAL(12,2),
    bonus_count INT,
    bonus_value DECIMAL(12,2),
    bonus_commission DECIMAL(12,2),
    total_count INT,
    total_value DECIMAL(12,2),
    total_commission DECIMAL(12,2),
    declined_count INT,
    declined_value DECIMAL(12,2),
    declined_commission DECIMAL(12,2),
    start_date DATE,
    end_date DATE,
    )
;

CREATE TABLE advertiser_performance_reports (
    report_id SERIAL PRIMARY KEY,
    advertiser_id INT,
    publisher_id INT,
    region_id INT,
    currency_id INT,
    impressions INT,
    clicks INT,
    pending_count INT,
    pending_value DECIMAL(12,2),
    pending_commission DECIMAL(12,2),
    confirmed_count INT,
    confirmed_value DECIMAL(12,2),
    confirmed_commission DECIMAL(12,2),
    bonus_count INT,
    bonus_value DECIMAL(12,2),
    bonus_commission DECIMAL(12,2),
    total_count INT,
    total_value DECIMAL(12,2),
    total_commission DECIMAL(12,2),
    declined_count INT,
    declined_value DECIMAL(12,2),
    declined_commission DECIMAL(12,2),
    start_date DATE,
    end_date DATE,
    )
;

CREATE TABLE publisher_campaign_report(
    date_id DATE,
    publisher_id INT,
    campaign VARCHAR,
    quantity INT,
    sale_value DECIMAL(12,2),
    commission_value DECIMAL(12,2),
    PRIMARY KEY(date_id, campaign),
)
;

CREATE TABLE advertiser_campaign_report(
    date_id DATE,
    advertiser_id INT,
    campaign VARCHAR,
    quantity INT,
    sale_value DECIMAL(12,2),
    commission_value DECIMAL(12,2),
    PRIMARY KEY(date_id, campaign),
)
;

CREATE TABLE advertiser_creative_report(
    report_id INT PRIMARY KEY,
    advertiser_id INT,
    publisher_id INT,
    region_id INT,
    currency_id INT,
    impressions INT,
    clicks INT,
    creative_id INT,
    tag_id INT,
    pending_count INT,
    pending_value DECIMAL(12,2),
    pending_commission DECIMAL(12,2),
    confirmed_count INT,
    confirmed_value DECIMAL(12,2),
    confirmed_commission DECIMAL(12,2),
    bonus_count INT,
    bonus_value DECIMAL(12,2),
    bonus_commission DECIMAL(12,2),
    total_count INT,
    total_value DECIMAL(12,2),
    total_commission DECIMAL(12,2),
    declined_count INT,
    declined_value DECIMAL(12,2),
    declined_commission DECIMAL(12,2),
    start_date DATE,
    end_date DATE,
)
;

CREATE TABLE publisher_creative_report(
    report_id INT PRIMARY KEY,
    publisher_id INT,
    advertiser_id INT,
    region_id INT,
    currency_id INT,
    impressions INT,
    clicks INT,
    creative_id INT,
    tag_id INT,
    pending_count INT,
    pending_value DECIMAL(12,2),
    pending_commission DECIMAL(12,2),
    confirmed_count INT,
    confirmed_value DECIMAL(12,2),
    confirmed_commission DECIMAL(12,2),
    bonus_count INT,
    bonus_value DECIMAL(12,2),
    bonus_commission DECIMAL(12,2),
    total_count INT,
    total_value DECIMAL(12,2),
    total_commission DECIMAL(12,2),
    declined_count INT,
    declined_value DECIMAL(12,2),
    declined_commission DECIMAL(12,2),
    start_date DATE,
    end_date DATE,
)
;

CREATE TABLE publisher(
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR,
)
;

CREATE TABLE tag(
    tag_id SERIAL PRIMARY KEY,
    tag VARCHAR,
)
;

CREATE TABLE advertiser(
    advertiser_id INT PRIMARY KEY,
    advertiser_name VARCHAR,
)
;

CREATE TABLE region(
    region_id INT PRIMARY KEY,
    region_name VARCHAR,
)
;

CREATE TABLE currency(
    currency_id INT PRIMARY KEY,
    currency_name VARCHAR,
    currency_code VARCHAR,
)
;

CREATE TABLE date(
    date_id DATE PRIMARY KEY.
    year INT,
    month INT,
    day INT,
    day_of_week INT,
    day_name VARCHAR,
    month_name VARCHAR,
    quarter INT,
)
;

CREATE TABLE creative(
    creative_id INT PRIMARY KEY,
    creative_name VARCHAR
)
;

CREATE TABLE publisher_tag_junction(
    publisher_id INT,
    tag_id INT,
    PRIMARY KEY (publisher_id, tag_id)
)
;

CREATE TABLE creative_tag_junction(
    creative_id INT,
    tag_id INT,
    PRIMARY KEY (creative_id, tag_id)
)
;
