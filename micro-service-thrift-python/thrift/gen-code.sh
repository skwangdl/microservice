#!/usr/bin/env bash
thrift --gen py -out ../src/ message.thrift
thrift --gen java -out ../../micro-service/src/main/java message.thrift