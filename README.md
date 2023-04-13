The project should be cloned into your working frontend project directory, as it utilizes the version specified in package.json.

It will generate a log file called vlog.txt, and output the following as an example:
```txt
[2023-02-17 19:37:28.878075] <product_name>: current: 2022.4.1, expected: 2022.4.2
```
Example of log:
```cmd
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Searching if version is deployed...
com.caseware.za.e.sme.2022: current: 2023.4.14, expected: 2023.4.15
Expected version updated: 2023.4.14
Expected version updated: 2023.4.14
Expected version updated: 2023.4.14
Expected version updated: 2023.4.15
Expected version updated: 2023.4.15
```

# Document Tree
```xml
<pluginUrls>
<pluginUrl url="http://.......&version=2022.4.1-dev.6"/>
...
...
</pluginUrls>
```
