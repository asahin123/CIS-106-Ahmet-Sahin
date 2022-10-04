<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Ahmet Halid Sahin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2022-10-04 06:42:11 AM"/>
        <attribute name="created" value="QWhtZXQgSGFsaWQgU2FoaW47REVTS1RPUC1ONjNJOFBOOzIwMjItMTAtMDI7MDc6NDM6MjggUE07Mzg3MA=="/>
        <attribute name="edited" value="QWhtZXQgSGFsaWQgU2FoaW47REVTS1RPUC1ONjNJOFBOOzIwMjItMTAtMDI7MDg6MjU6MzcgUE07MTtBaG1ldCBIYWxpZCBTYWhpbjtERVNLVE9QLU42M0k4UE47MjAyMi0wOS0xOTswNDozNzoxNiBQTTtkaXN0YW5jZSBjb252ZXJ0ZXIgd2l0aCBmdW5jdGlvbnMuZnByZzsxMTgwOQ=="/>
        <attribute name="edited" value="QWhtZXQgSGFsaWQgU2FoaW47REVTS1RPUC1ONjNJOFBOOzIwMjItMTAtMDQ7MDY6NDI6MTEgQU07NjszOTYw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <comment text="This program asks the user to select US or Metric conversion and input a given distance. Then the program converts the given distance to miles and displays the result."/>
            <declare name="miles" type="Real" array="False" size=""/>
            <declare name="choice" type="String" array="False" size=""/>
            <assign variable="miles" expression="getInputMiles()"/>
            <assign variable="choice" expression="getChoiceChar()"/>
            <if expression="choice = &quot;U&quot; or choice = &quot;u&quot;">
                <then>
                    <call expression="ProcessUSdistance(miles)"/>
                </then>
                <else>
                    <if expression="choice = &quot;M&quot; or choice = &quot;m&quot;">
                        <then>
                            <call expression="processMetricDistance(miles)"/>
                        </then>
                        <else>
                            <output expression="&quot;You must enter U to convert distance into US distance or M to convert into Metric distance!&quot;" newline="True"/>
                        </else>
                    </if>
                </else>
            </if>
            <comment text="References: https://www.youtube.com/watch?v=VcZG_PxP7wQ&amp;t=34s"/>
        </body>
    </function>
    <function name="calculateCentimeters" type="Real" variable="centimeters">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="centimeters" type="Real" array="False" size=""/>
            <assign variable="centimeters" expression="miles*160934.4"/>
        </body>
    </function>
    <function name="calculateFeet" type="Real" variable="feet">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="feet" type="Real" array="False" size=""/>
            <assign variable="feet" expression="miles*5280"/>
        </body>
    </function>
    <function name="calculateInches" type="Real" variable="inches">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="Inches" type="Real" array="False" size=""/>
            <assign variable="inches" expression="miles*63360"/>
        </body>
    </function>
    <function name="calculateKilometers" type="Real" variable="kilometers">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="kilometers" type="Real" array="False" size=""/>
            <assign variable="kilometers" expression="miles*1.609344"/>
        </body>
    </function>
    <function name="calculateMeters" type="Real" variable="meters">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="meters" type="Real" array="False" size=""/>
            <assign variable="meters" expression="miles*1609.344"/>
        </body>
    </function>
    <function name="calculateYards" type="Real" variable="yards">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="yards" type="Real" array="False" size=""/>
            <assign variable="yards" expression="miles*1760"/>
        </body>
    </function>
    <function name="displayResult" type="None" variable="">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
            <parameter name="kMyD" type="Real" array="False"/>
            <parameter name="strKm" type="String" array="False"/>
            <parameter name="mTfT" type="Real" array="False"/>
            <parameter name="strM" type="String" array="False"/>
            <parameter name="cMiN" type="Real" array="False"/>
            <parameter name="strCm" type="String" array="False"/>
        </parameters>
        <body>
            <output expression="miles &amp; &quot; mile(s) is equivalent to &quot; &amp; kMyD &amp; strKm &amp; mTfT &amp; strM &amp; cMiN &amp; strCm" newline="True"/>
        </body>
    </function>
    <function name="getChoiceChar" type="String" variable="choice">
        <parameters/>
        <body>
            <declare name="choice" type="String" array="False" size=""/>
            <output expression="&quot;Enter U to convert to US distance or M to convert to Metric distance.&quot;" newline="True"/>
            <input variable="choice"/>
        </body>
    </function>
    <function name="getInputMiles" type="Real" variable="miles">
        <parameters/>
        <body>
            <output expression="&quot;Enter distance in terms of miles&quot;" newline="True"/>
            <declare name="miles" type="Real" array="False" size=""/>
            <input variable="miles"/>
        </body>
    </function>
    <function name="processMetricDistance" type="None" variable="">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="kilometers" type="Real" array="False" size=""/>
            <declare name="meters" type="Real" array="False" size=""/>
            <declare name="centimeters" type="Real" array="False" size=""/>
            <assign variable="kilometers" expression="calculateKilometers(miles)"/>
            <assign variable="meters" expression="calculateMeters(miles)"/>
            <assign variable="centimeters" expression="calculateCentimeters(miles)"/>
            <call expression="displayResult(miles, kilometers, &quot; km, &quot;, meters, &quot; m, &quot;, centimeters, &quot; cm.&quot;)"/>
        </body>
    </function>
    <function name="ProcessUsDistance" type="None" variable="">
        <parameters>
            <parameter name="miles" type="Real" array="False"/>
        </parameters>
        <body>
            <declare name="yards" type="Real" array="False" size=""/>
            <declare name="feet" type="Real" array="False" size=""/>
            <declare name="inches" type="Real" array="False" size=""/>
            <assign variable="yards" expression="calculateYards(miles)"/>
            <assign variable="feet" expression="calculateFeet(miles)"/>
            <assign variable="inches" expression="calculateInches(miles)"/>
            <output expression="miles &amp; &quot; mile(s) is equivalent to &quot; &amp; yards &amp; &quot; yards, &quot; &amp; feet &amp; &quot; ft, &quot; &amp; inches &amp; &quot; inches&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>
