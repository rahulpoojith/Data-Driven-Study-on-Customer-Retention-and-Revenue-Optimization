-- public.vw_monthly_churn source

CREATE OR REPLACE VIEW public.vw_monthly_churn
AS SELECT experiment_group,
    activity_month,
    round(sum(churned)::numeric / count(*)::numeric, 4) AS churn_rate
   FROM vw_customer_monthly
  GROUP BY experiment_group, activity_month;
