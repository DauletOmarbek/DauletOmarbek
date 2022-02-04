CREATE OR REPLACE FUNCTION timestamp()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.last_name <> OLD.last_name THEN
		 INSERT INTO last_time(employee_id,time,changed_on)
		 VALUES(OLD.id,OLD.time,now());
	END IF;

	RETURN NEW;
END;
$$


CREATE TRIGGER time_changes
  BEFORE UPDATE
  ON real_time
  FOR EACH ROW
  EXECUTE PROCEDURE timestamp();

UPDATE real_time
SET time = 20
WHERE ID = 2;