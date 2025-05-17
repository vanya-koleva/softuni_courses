function solve(browser, actions) {
    const openTabs = browser['Open Tabs'];
    const recentlyClosed = browser['Recently Closed'];
    const logs = browser['Browser Logs'];

    for (let action of actions) {
        if (action === 'Clear History and Cache') {
            openTabs.length = 0;
            recentlyClosed.length = 0;
            logs.length = 0;
        } else {
            const [command, ...siteParts] = action.split(' ');
            const site = siteParts.join(' ');

            if (command === 'Open') {
                openTabs.push(site);
                logs.push(action);
            } else if (command === 'Close') {
                const index = openTabs.indexOf(site);

                if (index !== -1) {
                    openTabs.splice(index, 1);
                    recentlyClosed.push(site);
                    logs.push(action);
                }
            }
        }
    }

    console.log(browser['Browser Name']);
    console.log(`Open Tabs: ${browser['Open Tabs'].join(', ')}`);
    console.log(`Recently Closed: ${browser['Recently Closed'].join(', ')}`);
    console.log(`Browser Logs: ${browser['Browser Logs'].join(', ')}`);
}

// solve(
//     {
//         'Browser Name': 'Google Chrome',
//         'Open Tabs': ['Facebook', 'YouTube', 'Google Translate'],
//         'Recently Closed': ['Yahoo', 'Gmail'],
//         'Browser Logs': [
//             'Open YouTube',
//             'Open Yahoo',
//             'Open Google Translate',
//             'Close Yahoo',
//             'Open Gmail',
//             'Close Gmail',
//             'Open Facebook',
//         ],
//     },
//     ['Close Facebook', 'Open StackOverFlow', 'Open Google']
// );

