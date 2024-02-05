-- Sample SQL script for performance tuning

-- Example: Increase shared_buffers
-- ALTER SYSTEM SET shared_buffers = '256MB';

-- Example: Tune autovacuum settings
-- ALTER SYSTEM SET autovacuum_analyze_scale_factor = 0.02;
-- ALTER SYSTEM SET autovacuum_vacuum_scale_factor = 0.05;
-- ALTER SYSTEM SET autovacuum_vacuum_cost_limit = 2000;

-- Example: Adjust maintenance_work_mem
-- ALTER SYSTEM SET maintenance_work_mem = '256MB';
