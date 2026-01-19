-- public.vw_monthly_arpu source

CREATE OR REPLACE VIEW public.vw_monthly_arpu
AS SELECT experiment_group,
    activity_month,
    round(avg(revenue), 2) AS arpu
   FROM vw_customer_monthly
  GROUP BY experiment_group, activity_month;

