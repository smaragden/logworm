#!/bin/bash
abspath=$(cd ${0%/*} && echo $PWD/${0##*/})
SCRIPTDIR=`dirname "$abspath"`
echo $SCRIPTDIR

RENDERER="arnold"
if [ $1 = $RENDERER ]; then
   while read line
   do
      sleep 0.01
      echo $line
   done <${SCRIPTDIR}/arnold_log.txt
fi

RENDERER="mr"
if [ $1 = $RENDERER ]; then
   while read line
   do
      sleep 0.01
      echo $line
   done <${SCRIPTDIR}/mr_log.txt
fi


