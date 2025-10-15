CREATE OR REPLACE FUNCTION get_logs_food(input_user_id text, input_date_added timestamptz)
RETURNS TABLE(
    date_added timestamptz,
    meal_name text,
    ingredient_name text,
    quantity numeric,
    serving_name text,
    serving_size_g numeric,
    weight_g numeric,
    total_calories_kcal numeric,
    total_fat_g numeric,
    total_carbs_g numeric,
    total_protein_g numeric
)
AS $$
    with food_logs_filtered as (
        select * from public.food_logs
        where user_id = input_user_id and date_added = input_date_added
    )

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

    from food_logs_filtered as fl

    join public.meals as m
        on fl.meal_id = m.id
    join public.ingredients as i
        on fl.ingredient_id = i.id
    join public.servings as s
        on fl.serving_id = s.id
$$ LANGUAGE SQL;
