--1)Increments given values by 1 and returns it.
create FUNCTION inc1(val integer) returns integer as
    $$
    BEGIN
        RETURN val + 2;
    END;
    $$
        LANGUAGE plpgsql;

select inc1(6);

drop function inc1;

--2)Returns sum of 2 numbers.
create FUNCTION inc2(val1 integer, val2 integer) returns integer as
    $$
    BEGIN
        RETURN val1 + val2;
    END;
    $$
        LANGUAGE plpgsql;

select inc2(4,52);

drop function inc2;

--3)Returns true or false if numbers are divisible by 2.
create function inc3(val integer) returns bool as
    $$
    begin
        if val%2 = 0 then
            return true;
        else
            return false;
        end if;
    end;
    $$
        language plpgsql;

select inc3(31);

drop function inc3;

--4)Checks some password for validity. ??
create function inc4(val char) returns bool as
    $$
    begin
        if (char_length(val) >= 8) then
            return true;
        else
            return false;
        end if;
    end;
    $$
        language plpgsql;

select inc4('abcdasd');

drop function inc4;

--5)Returns two outputs, but has one input. ??
create function inc5(val integer) returns integer as
    $$
    begin
        return val;
    end;
    $$
        language plpgsql;

select inc5(123);

drop function inc5;

