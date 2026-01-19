-- public.vw_quarter_summary source

CREATE OR REPLACE VIEW public.vw_quarter_summary
AS SELECT experiment_group,
    count(DISTINCT customer_id) AS customers,
    sum(churned) AS churned_customers,
    round(sum(churned)::numeric / count(DISTINCT customer_id)::numeric, 4) AS churn_rate,
    round(avg(total_revenue), 2) AS avg_revenue
   FROM vw_customer_level
  GROUP BY experiment_group;

