-- public.vw_customer_level source

CREATE OR REPLACE VIEW public.vw_customer_level
AS SELECT customer_id,
    experiment_group,
    max(churned) AS churned,
    sum(revenue) AS total_revenue
   FROM vw_customer_monthly
  GROUP BY customer_id, experiment_group;
