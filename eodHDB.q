r:-11!(-2;.u.L);
-11!(r;.u.L);

agg:-5#agg;
quoteCols:`,((cols quote)except `time`sym);
tradeCols:`,((cols trade)except `time`sym);
aggCols:`,((cols trade)except `time`sym);

count aggCols
date:.z.d;

(hsym ` sv (`:hdb;`trade;`$(string date));tradeCols!((17;2;9);(17;2;6);(17;2;6);(17;2;6))) set .Q.en[`:.]trade;
(hsym ` sv (`:hdb;`quote;`$(string date));quoteCols!((17;2;9);(17;2;6);(17;2;6);(17;2;6);(17;2;6);(17;2;6))) set .Q.en[`:.]quote;
(hsym ` sv (`:hdb;`agg;`$(string date));aggCols!((17;2;9);(17;2;6);(17;2;6);(17;2;6))) set .Q.en[`:.]agg;


