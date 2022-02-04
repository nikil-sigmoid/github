#!/bin/bash

python api_call.py $1> result.log
cat result.log

result=$(tail -1 result.log)
IFS="," read -r PREVIOUS_SHA CURRENT_SHA<<< "${result}"
echo $PREVIOUS_SHA
echo $CURRENT_SHA

echo "Files changed:"
git diff --name-status $PREVIOUS_SHA $CURRENT_SHA

ADDED=$(git diff --diff-filter=A --name-only "$PREVIOUS_SHA" "$CURRENT_SHA" | awk -v d=" " '{s=(NR==1?s:s d)$0}END{print s}')
MODIFIED=$(git diff --diff-filter=M --name-only "$PREVIOUS_SHA" "$CURRENT_SHA" | awk -v d=" " '{s=(NR==1?s:s d)$0}END{print s}')
DELETED=$(git diff --diff-filter=D --name-only "$PREVIOUS_SHA" "$CURRENT_SHA" | awk -v d=" " '{s=(NR==1?s:s d)$0}END{print s}')

echo "added files: $ADDED"
echo "modified files: $MODIFIED"
echo "deleted files: $DELETED"