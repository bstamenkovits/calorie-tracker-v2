create or replace view public.logs_food as (
    select
        -- when
        fl.date_added as date_added,
        m.name as meal_name,

        -- what
        i.name as ingredient_name,
        fl.quantity as quantity,
        s.name as serving_name,
        s.size_g as serving_size_g,

        -- nutrition
        fl.quantity * s.size_g as weight_g,
        (fl.quantity * s.size_g) / 100.0 * i.calories_kcal as total_calories_kcal,
        (fl.quantity * s.size_g) / 100.0 * i.fat_g as total_fat_g,
        (fl.quantity * s.size_g) / 100.0 * i.carbs_g as total_carbs_g,
        (fl.quantity * s.size_g) / 100.0 * i.protein_g as total_protein_g

    from public.food_logs as fl

    join public.meals as m
        on fl.meal_id = m.id
    join public.ingredients as i
        on fl.ingredient_id = i.id
    join public.servings as s
        on fl.serving_id = s.id
);
