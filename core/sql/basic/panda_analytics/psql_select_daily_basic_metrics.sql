SELECT '{
  "s": "May 7, 2024",
  "fontsize": 10,
  "alpha": 0.8
}'::jsonb AS        date,
       '[
         {
           "metric": {
             "s": "Оборот",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "105.04k",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 27%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         },
         {
           "metric": {
             "s": "Заказы",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "505",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 5%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         },
         {
           "metric": {
             "s": "Средний чек",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "2,120",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 12%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         },
         {
           "metric": {
             "s": "Остатки на складах",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "45%%",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 2%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма возвратов",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "15,000",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 18%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         },
         {
           "metric": {
             "s": "Доля возвратов",
             "fontsize": 10,
             "alpha": 0.7
           },
           "value": {
             "s": "5%%",
             "fontsize": 17,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 11%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,rounding_size=0.7"
             }
           }
         }
       ]'::jsonb AS metrics
;
