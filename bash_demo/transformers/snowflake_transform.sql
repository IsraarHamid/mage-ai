-- Docs: https://docs.mage.ai/guides/sql-blocks
CREATE 
OR REPLACE VIEW IF NOT EXISTS TEST.PRD.RECIPE AS 
SELECT 
  * 
FROM 
  TEST.RAW.RECIPES_RAW;
