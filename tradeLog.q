/   tradeLog.q

r:get .u.L;

LL:`:tradeLog;
if[not type key LL;.[LL;();:;()]];
ll::hopen LL

{ll enlist x} each r where {`trade in x}each r