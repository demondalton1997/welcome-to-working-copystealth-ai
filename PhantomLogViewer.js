// PhantomLogViewer.js
const fs = $file.read("logs/log.txt");
$ui.alert(fs ? fs.string : "No logs found");
