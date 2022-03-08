DATE_TODAY=$(date +"%Y-%m-%d")

function isHeadAuthorDateToday() {
    headAuthorDate=$(git --no-pager log -n 1 --pretty=format:%ai | cut -f 1 -d ' ')
    if [[ $headAuthorDate = $DATE_TODAY ]]; then
        return 0
    else
        return 1
    fi
}

function isHeadGeneratedByLeethub() {
    headMsg=$(git --no-pager log -n 1 --pretty=format:%B)
    if [[ $headMsg == *"LeetHub"* ]]; then
        return 0
    else
        return 1
    fi
}


anyUnstaged=0
while isHeadAuthorDateToday && isHeadGeneratedByLeethub
do
    git reset --soft HEAD~1
    anyUnstaged=1
done

if [[ $anyUnstaged -eq 1 ]]; then
    git add -A
    git commit -m "${DATE_TODAY} - LeetHub"
fi
