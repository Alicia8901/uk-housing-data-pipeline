SELECT *
FROM `uk-housing-data-pipeline.housing_data.housing_raw`
LIMIT 10;

-- Creating Analytics Table
CREATE OR REPLACE TABLE `uk-housing-data-pipeline.housing_data.housing_analytics` AS
SELECT
  *,
  EXTRACT(YEAR FROM date) AS sale_year,
  EXTRACT(MONTH FROM date) AS sale_month
FROM `uk-housing-data-pipeline.housing_data.housing_raw`;

-- Average Price by Year
SELECT
  sale_year,
  ROUND(AVG(price), 2) AS average_price
FROM `uk-housing-data-pipeline.housing_data.housing_analytics`
GROUP BY sale_year
ORDER BY sale_year;

-- Average Price by Property Type
SELECT
  property_type,
  ROUND(AVG(price), 2) AS average_price
FROM `uk-housing-data-pipeline.housing_data.housing_analytics`
GROUP BY property_type
ORDER BY average_price DESC;

-- Top Districts
SELECT
  district,
  ROUND(AVG(price), 2) AS average_price
FROM `uk-housing-data-pipeline.housing_data.housing_analytics`
GROUP BY district
ORDER BY average_price DESC
LIMIT 10;

