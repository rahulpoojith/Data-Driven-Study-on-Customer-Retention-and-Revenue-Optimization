-- public.vw_ab_test_data source

CREATE OR REPLACE VIEW public.vw_ab_test_data
AS SELECT experiment_group,
    customer_id,
    churned,
    total_revenue
   FROM vw_customer_level;
