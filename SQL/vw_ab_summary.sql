-- public.vw_ab_summary source

CREATE OR REPLACE VIEW public.vw_ab_summary
AS SELECT experiment_group,
    count(*) AS total_customers,
    sum(churned) AS churned_customers,
    round(sum(churned)::numeric / count(*)::numeric, 4) AS churn_rate,
    round(1::numeric - sum(churned)::numeric / count(*)::numeric, 4) AS retention_rate,
    round(avg(total_revenue), 2) AS arpu
   FROM vw_customer_level
  GROUP BY experiment_group;
