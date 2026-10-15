#submitted by noor in 14 oct
SELECT current_weather.id
FROM Weather current_weather
JOIN Weather previous_weather
  ON DATEDIFF(current_weather.recordDate, previous_weather.recordDate) = 1
WHERE current_weather.temperature > previous_weather.temperature;
