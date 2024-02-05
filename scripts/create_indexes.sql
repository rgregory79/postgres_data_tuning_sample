-- Sample SQL script to create indexes
CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_orders_order_date ON orders(order_date); 
CREATE INDEX IF NOT EXISTS idx_orders_order_date ON orders(order_date); 
