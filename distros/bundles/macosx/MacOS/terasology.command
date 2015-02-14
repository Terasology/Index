#!/bin/bash
cd "$(dirname "$0")/../Resources/"
jre/bin/java -Xms128m -Xmx1024m -jar libs/Terasology.jar
