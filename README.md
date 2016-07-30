###1. 下载 elasticsearch

```
    https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.4/elasticsearch-2.3.4.tar.gz
```

###2. 下载 elastisearch-jdbc

```
    https://github.com/jprante/elasticsearch-jdbc
```

###3．设置elasticsearch-jdbc

```
    export JDBC_IMPORTER_HOME=path_of_elasticsearch_jdbc
    bin=$JDBC_IMPORTER_HOME/bin
    lib=$JDBC_IMPORTER_HOME/lib
```

###4.编写elasticsearch-jdbc-import文件,文件名[jdbc_importer_1],内容如下

```
    {
        "type": "jdbc",
        "jdbc": {
            "url": "jdbc:mysql://127.0.0.1:3306/test",
            "user": "root",
            "password": "123456",
            "sql": "select * from orders",
            "index": "myindex",
            "type": "mytype"
        }
    }
```

###5.在mysql导入数据

```
    mysql -h127.0.0.1 -uroot -p123456 test < orders.sql
```

###6.运行elasticsearch

```
    cd elasticsearch-2.3.3
    bin/elasticsearch
```

###6.执行导入mysql数据到elasticsearch

```
    java \
        -cp "${lib}/*" \
        -Dlog4j.configurationFile=${bin}/log4j2.xml \
        org.xbib.tools.Runner \
        org.xbib.tools.JDBCImporter \
        jdbc_importer_1
```
###7.运行elasticsearch demo

```
    pip install elasticsearch
    cd elasticsearch_demo
     python test_bulk.py
     python test_elk_curd.py
```
