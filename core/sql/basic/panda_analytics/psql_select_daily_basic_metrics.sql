SELECT '{
  "s": "Ежедневный отчёт: 12 Мая, 2024",
  "fontsize": 10,
  "alpha": 0.8
}'::jsonb AS        date,
       '[
         {
           "metric": {
             "s": "Сумма продаж",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "633.91k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 38%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Количество продаж",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "381",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 38%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма возвратов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "17.22k",
             "fontsize": 15,
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
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Средний %% возвратов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "2.00%%",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 26%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Логистика",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "16.79k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 13%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма штрафов",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "630",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 301%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Сумма комиссии",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "130.73k",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↑ 37%%",
             "fontsize": 7,
             "color": "red",
             "bbox": {
               "facecolor": "red",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         },
         {
           "metric": {
             "s": "Средний %% комиссии",
             "fontsize": 8,
             "alpha": 0.7
           },
           "value": {
             "s": "21.20%%",
             "fontsize": 15,
             "fontweight": "bold"
           },
           "change": {
             "s": "↓ 1%%",
             "fontsize": 7,
             "color": "green",
             "bbox": {
               "facecolor": "green",
               "edgecolor": "grey",
               "alpha": 0.15,
               "linewidth": 0.1,
               "boxstyle": "round,pad=0.6,rounding_size=1"
             }
           }
         }
       ]'::jsonb AS metrics
;
