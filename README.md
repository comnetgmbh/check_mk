# SAP cloud connector check


## Description
Check_MK agent for the monitoring API of the SAP Cloud Connector.
Documentation of the monitoring API can be found at the following
URL:
https://help.sap.com/viewer/cca91383641e40ffbe03bdc78f00f681/Cloud/en-US/f6e7a7bc6af345d2a334c2427a31d294.html
This agent utilizes the python "requests" library to query the
SAP Cloud Connector monitoring API via HTTP/S.

This agent currently queries the following endpoints of the SAP
Cloud Connector monitoring API via HTTP/S:
/api/monitoring/subaccounts
/api/monitoring/connections/backends
/api/monitoring/performance/backends
/api/monitoring/performance/toptimeconsumers

It parses the JSON data returned from those endpoints and trans-
forms it into a flattened key, value list. This list is sub-
sequently printed for further processing of the data by Check_MK
check scripts.

This agent has currently been verified to work with the following
versions of the SAP Cloud Connector:
Version: 2.11.2


## SAP Cloud Connector Backend Performance
```
This check monitors the performance of each (on-premise) backend system
connected to a SAP Cloud Connector instance.

The backend performance metrics are grouped into 22 buckets for each
backend system by the SAP Cloud Connector monitoring API. In each bucket,
those backend calls are counted whose runtime matches the buckets timing
window definitions.

The following metrics are provided by this check:

{calls_total} The rate (calls per second) of overall calls. The absolute
number of overall calls is also reportet in the service state.

{calls_min_10_ms}, {calls_min_20_ms}, {calls_min_30_ms}, {calls_min_40_ms},
{calls_min_50_ms}, {calls_min_75_ms}, {calls_min_100_ms}, {calls_min_125_ms},
{calls_min_150_ms}, {calls_min_200_ms}, {calls_min_300_ms}, {calls_min_400_ms},
{calls_min_500_ms}, {calls_min_750_ms}, {calls_min_1000_ms}, {calls_min_1250_ms},
{calls_min_1500_ms}, {calls_min_2000_ms}, {calls_min_2500_ms}, {calls_min_3000_ms},
{calls_min_4000_ms}, {calls_min_5000_ms} The individual call rate for
each of the buckets.

With the two thresholds {runtime_warning} and {runtime_critical} the calls
in the above buckets are devided in three sets: {calls_ok} for the sum of
all calls in buckets with a runtime lower than {runtime_warning}, {calls_warn}
for the sum of all calls in buckets with a runtime higher than {runtime_warning}
and lower than {runtime_critical} and {calls_crit} for the sum of all calls
in buckets with a runtime higher than {runtime_critical}.

The metrics {calls_pct_ok}, {calls_pct_warn}, {calls_pct_crit} provide the
relative amount of calls in each of the three sets. The relative number
of calls in the set {calls_pct_warn} is compared to the {warning} threshold.
The relative number of calls in the set {calls_pct_crit} is compared to
the {critical} threshold.

Default levels for warning and critical {runtime} are 500 and 1000 milliseconds.
Default levels for warning and critical {percentage} are 10 and 5 percent.
These are configurable via WATO.
```

## SAP Cloud Connector Subaccount: Application Connection
```
This check determines {subaccount} information on a SAP Cloud Connector
instance. It which work on the same data as the checks {sapcc_subaccounts.info}
and {sapcc_subaccounts.tunnel}. The data is gathered from the Check_MK
special agent {agent_sapcc} for the SAP Cloud Connector.

{sapcc_subaccounts.app_conn} gathers performance information on each
application connection of each tunnel of each subaccount defined on a
SAP Cloud Connector instance. It raises an alarm if the {number of
connections} are below or above of a configured threshold.

The warning and critical threshold values in {number of connections}
are configurable via WATO.
```

## SAP Cloud Connector Subaccount: Info
```
This check determines {subaccount} information on a SAP Cloud Connector
instance. It which work on the same data as the checks {sapcc_subaccounts.tunnel}
and {sapcc_subaccounts.app_conn}. The data is gathered from the Check_MK
special agent {agent_sapcc} for the SAP Cloud Connector.

{sapcc_subaccounts.info} just gathers information on each subaccount
defined on a SAP Cloud Connector instance. The collected attributes are
the {displayName}, the {locationID} and the {regionHost}. It prints this
information in the status details of the check and has no threshold checks
or performance data. The check status is always {OK}.
```

## SAP Cloud Connector Subaccount: Tunnel
```
This check determines {subaccount} information on a SAP Cloud Connector
instance. It which work on the same data as the checks {sapcc_subaccounts.info}
and {sapcc_subaccounts.app_conn}. The data is gathered from the Check_MK
special agent {agent_sapcc} for the SAP Cloud Connector.

{sapcc_subaccounts.tunnel} gathers status and performance information
on the tunnel of each subaccount defined on a SAP Cloud Connector instance.
It raises an alarm if the {status} of the tunnel is not {Connected} or
if the {number of connections} are below or above of a configured threshold.
An alarm is also raised if the tunnel connection is present for a less
or more {time} than a configured threshold.

The warning and critical threshold values in {number of connections}
and {seconds of connection time} are configurable via WATO.
```
