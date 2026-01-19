-- public.vw_customer_monthly source

CREATE OR REPLACE VIEW public.vw_customer_monthly
AS SELECT act.customer_id,
    act.activity_month,
    ca.experiment_group,
    act.churned,
    act.revenue
   FROM customer_activity act
     JOIN campaign_assignment ca ON act.customer_id = ca.customer_id;



