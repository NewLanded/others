<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>lyb</title>
    <style type='text/css'>
        .xmlName{
            margin:2px 42px 0px 5px;
            float:left;
            }
        .xmlButton{
            margin:2px 42px 5px 5px;
            }
    </style>
</head>
<body>

% for key in xmlInfo:
    <div>
        <div class="xmlName">{{key}}</div>
        <div class="xmlButton">
            <input type="button" id={{key}} value="send XML" onclick="sendXml(this)"></input>
        </div>
        <div>
            <textarea id={{key}} name={{key}} class="xml" cols="100" rows="20" spellcheck="false">
                {{xmlInfo[key]}}
            </textarea>
        </div>
    </div>
% end

% for key in natpInfo:
    <div>
        <div class="xmlName">{{key}}</div>
        <div class="xmlButton">
            <input type="button" id={{key}} value="send NATP" onclick="sendNatp(this)"></input>
        </div>
        <div>
            <textarea id={{key}} name={{key}} class="natp" cols="100" rows="20" spellcheck="false">
                {{natpInfo[key]}}
            </textarea>
        </div>
    </div>
% end

    <script type="text/javascript" src="/static/jquery-3.0.0.js"></script>
    <script type="text/javascript" src="/static/xml.js"></script>
</body>
