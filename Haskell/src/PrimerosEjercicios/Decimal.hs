
module Decimal where

import Data.Char;

-- Pasar numero decimal y sacar por un lado la parte real y la otra decimal
-- 3.1416 ... por 100 314,16 ... truncar 314 ... el original truncado por 100, y restar ese 300

separarReal :: Float -> (Integer, Integer)
separarReal m = (truncate m , truncate(m*100)- (truncate m)*100 )
