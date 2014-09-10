#!/bin/sh
export CURRENTDIR='/home/lingfeiyou/ShareTest/TopAPI/workspace/TOP_API'
export JAVA_HOME=/usr/lib/jvm/default-java
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:${JRE_HOME}/bin:$PATH:/home/lingfeiyou/ShareTest/apache-jmeter-2.9/bin:/usr/bin
export JMETER="/home/lingfeiyou/ShareTest/apache-jmeter-2.9"
export CLASSPATH="$JMETER/lib/ext/ApacheJMeter_core.jar:$JMETER/lib/jorphan.jar:$JMETER/lib/logkit-2.0.jar:$CLASSPATH"

echo CURRENTDIR=$CURRENTDIR
echo +++++++++++++++++++++
echo clean the last test results
echo ++++++++++++++++++++
rm -rf ${CURRENTDIR}/db.xml

echo start new test run
jmeter.sh -n -t ${CURRENTDIR}/db.jmx
