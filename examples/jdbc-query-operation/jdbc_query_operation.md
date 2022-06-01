# Simple query

This BBE demonstrates how to use the JDBC client select query operations
with the stream return type. Note that the relevant database driver JAR
should be defined in the `Ballerina.toml` file as a dependency.
This sample is based on an H2 database and the H2 database driver JAR need to be added to `Ballerina.toml` file.
For a sample configuration and more information on the underlying module, see the [JDBC module](https://docs.central.ballerina.io/ballerinax/java.jdbc/latest/) .<br><br>
This sample is written using H2 2.0.6 and it is recommended to use H2 JAR with versions higher than 2.0.2.

::: code ./examples/jdbc-query-operation/jdbc_query_operation.bal :::

::: out ./examples/jdbc-query-operation/jdbc_query_operation.out :::