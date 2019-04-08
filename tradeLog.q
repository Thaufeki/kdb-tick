/   tradeLog.q

r:get .u.L;

LL:`:tradeLog;
ll::hopen LL

{ll enlist x} each r where {`trade in x}each r;