-- this script creates a trigger
-- decreases quanitity of an item after getting a new order of that item
CREATE TRIGGER dec_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
