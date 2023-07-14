-- Write a SQL script that creates a trigger that decreases the quantity of
-- an item after adding a new order.

-- Quantity in the table items can be negative.

-- Context: Updating multiple tables for one action from your application can
-- generate issue: network disconnection, crash, etc… to keep your data in a
-- good shape, let MySQL do it for you!

CREATE TRIGGER before_insert_order
BEFORE INSERT ON orders
    FOR EACH ROW
        UPDATE items SET quantity = quantity - NEW.number
            WHERE name=NEW.item_name;
