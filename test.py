import requests
import uuid
import datetime

transactionId =  str(uuid.uuid4())
transactionId = 'NPC' + transactionId.replace('-', '')
messageId =  str(uuid.uuid4())
messageId = 'NPC' + messageId.replace('-', '')
ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+05:30"
print(ts)
# ts= datetime.datetime.now().astimezone().isoformat()
amount = "10000.00"
name = "TestMandate"
payervpa = "testvpa@oksbi"
payeeaddress = "testpayee@oksbi"
recurrance = "ONETIME"
url = "https://api.infinit.co.in/upi/2.0/ReqMandate/2.0/urn:txnid:" + transactionId
headers = {'Authorization': 'Bearer 084cbe55-72de-313b-93e3-040a2ab07da5', 'Content-Type' : 'application/xml'}
print(transactionId)
test = """
<upi:ReqMandate xmlns:upi="http://npci.org/upi/schema/">
    <Head ver="2.0" ts="{ts}" orgId="112233" msgId="{messageId}"/>
    <Meta>
        <Tag name="PAYREQSTART" value="{ts}"/>
        <Tag name="PAYREQEND" value="{ts}"/>
    </Meta>
    <Txn id="{txnId}" note="Mandate" custRef="722217098761" refId="XYA5447D86914C14AC1B0A4C4A036B387B3" purpose="00" refUrl="http://axis.com/upi" ts="2018-02-17T13:39:56.040+05:30" initiationMode="00" type="CREATE" refCategory="00" initiatedBy="PAYER">
        <Rules>
            <Rule name="EXPIREAFTER" value="10"/>
        </Rules>
    </Txn>
    <Mandate name="{name}" txnId="{txnId}" ts="{ts}" type="CREATE" umn="75979u79hyihighi8479579567967967@mypsp" shareToPayee="Y" revokeable="Y" blockFund="Y">
        <Amount value="{amount}" rule="EXACT"/>
        <Recurrence pattern="{recurrance}">
        </Recurrence>
    </Mandate>
    <Payer addr="{payervpa}" name="GOI" seqNum="1" type="ENTITY" code="0000">
        <Info>
            <Identity id="058010100083492" type="ACCOUNT" verifiedName="GOI"/>
            <Rating VerifiedAddress="TRUE"/>
        </Info>
        <Device>
            <Tag name="MOBILE" value="919999999993"/>
            <Tag name="TYPE" value="MOB"/>
            <Tag name="ID" value="61e402e8fa3e3450ca6e"/>
            <Tag name="OS" value="ios 2.0"/>
            <Tag name="APP" value="in.org.npci.bhim"/>
            <Tag name="LOCATION" value="3.993U49234902"/>
            <Tag name="GEOCODE" value="37.7934,12.4134"/>
        </Device>
        <Ac addrType="ACCOUNT">
            <Detail name="IFSC" value="AABF0001122"/>
            <Detail name="ACTYPE" value="CURRENT"/>
            <Detail name="ACNUM" value="0101222101223"/>
        </Ac>
        <Creds>
            <Cred type="PIN" subType="MPIN">
                <Data code="NPCI" ki="20150822">
                    2.0|OmTUd6Fb1zEHRjQJ0QD60ZxdwKHH0WrwUu+x5KrE2RhdF2u6Bzzt5Lx7tHMcsB+TMn9s3UOWxWulnduruRWGG5ihhgOjfCKOdAH42Ro5YnGo36yv3xvauIXpG0ZnrnjDoYWx7HcsHfxvsmlMDUEQ1UiTKlsb+Ze66IIr3AttZKfRTPuSUKqNjrCuSeEcv8X9xO5Wk2jUKO0SxD9/BMUv4QRw8uu9lZujMtc8oV/h1woCoc1F/x26pwZSsXEC+lUnAEnOzZF3ttUpT/JsiNTKs+G9Ta1mULQJcbZCQUWdx1xazaN2XuRpc8zeio51AsB4SQXBzRVa0tZgVfA3flajFQ==                                        
                </Data>
            </Cred>
        </Creds>
    </Payer>
    <Payees>
        <Payee addr="{payeeaddress}" name="NEERAJSHARMA" seqNum="1" type="PERSON" code="0000">
        </Payee>
    </Payees>
</upi:ReqMandate>
"""
o = test.format(payeeaddress=payeeaddress, payervpa=payervpa, name=name, amount =amount, txnId =transactionId, ts = ts , messageId = messageId, recurrance = recurrance)
print(o)
data = '<upi:ReqPay xmlns:upi="http://npci.org/upi/schema/"><Head ver="2.0" ts="2018-02-17T13:39:54.939+05:30" orgId="112233" msgId="'+messageId+'"/><Txn id="'+transactionId+'" note="testpay" custRef="804813039157" refId="804813039157" refUrl="http://axis.com/upi" ts="2018-02-17T13:39:54.944+05:30" type="PAY" initiationMode="12" purpose="00"/><Payer addr="ram@axis" name="ram" seqNum="1" type="ENTITY" code="0000"><Info><Identity id="058010100083492" type="ACCOUNT" verifiedName="Ram"/><Rating VerifiedAddress="TRUE"/></Info><Device><Tag name="MOBILE" value="918149033167"/><Tag name="GEOCODE" value="34.7273,74.8278"/><Tag name="LOCATION" value="pune"/><Tag name="IP" value="192.68.0.12"/><Tag name="TYPE" value="MOB"/><Tag name="ID" value="3356"/><Tag name="OS" value="ios"/><Tag name="APP" value="10000629091"/><Tag name="CAPABILITY" value="1234556789"/></Device><Ac addrType="ACCOUNT"><Detail name="ACTYPE" value="SAVINGS"/><Detail name="ACNUM" value="050000"/><Detail name="IFSC" value="IFSC3567655"/></Ac><Creds><Cred type="PIN" subType="MPIN"><Data code="NPCI" ki="20150822">base-64 encoded/encrypted authentication data</Data></Cred></Creds><Amount value="05.00" curr="INR"><Split name="PURCHASE" value="1"/></Amount></Payer><Payees><Payee addr="laxmi@boi" name="AS" seqNum="1" type="PERSON" code="4000"><Device><Tag name="MOBILE" value="918149033167"/><Tag name="GEOCODE" value="34.7273,74.8278"/><Tag name="LOCATION" value="pune"/><Tag name="IP" value="192.68.0.12"/><Tag name="TYPE" value="MOB"/><Tag name="ID" value="3356"/><Tag name="OS" value="ios"/><Tag name="APP" value="10000629091"/><Tag name="CAPABILITY" value="1234556789"/></Device><Amount value="05.00" curr="INR"><Split name="PURCHASE" value="1"/></Amount></Payee></Payees></upi:ReqPay>'
r = requests.post(url = url, data = o, headers =  headers)
print(r.content)