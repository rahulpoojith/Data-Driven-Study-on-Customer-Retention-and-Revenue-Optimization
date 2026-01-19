-- public.vw_monthly_retention source

CREATE OR REPLACE VIEW public.vw_monthly_retention
AS SELECT experiment_group,
    activity_month,
    round(1::numeric - sum(churned)::numeric / count(*)::numeric, 4) AS retention_rate
   FROM vw_customer_monthly
  GROUP BY experiment_group, activity_month;

