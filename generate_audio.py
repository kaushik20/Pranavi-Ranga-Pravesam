import os
from google.cloud import texttospeech

# Initialize client
client = texttospeech.TextToSpeechClient.from_service_account_json('path/to/your-service-account-key.json')

# Narration content
narration_content = {
    "hero": "శ్రీ ప్రణవి చింతలపూడి రంగప్రవేశానికి స్వాగతం! ఆమె కూచిపూడి తొలి ప్రదర్శనను జరుపుకోవడానికి మాతో చేరండి. ఆమె పదకొండు సంవత్సరాల కళాత్మక ప్రయాణాన్ని తెలుసుకోండి మరియు RSVP చేయండి.",
    "about": "శ్రీ ప్రణవి చింతలపూడి బిట్స్ పిలానీ, దుబాయ్ క్యాంపస్‌లో ఇంజనీరింగ్ విద్యార్థి మరియు కూచిపూడి నృత్యకారిణి. స్మత్. ప్రీతి తాంబోట్ల శిక్షణలో ఎనిమిది సంవత్సరాలుగా నృత్యం నేర్చుకుంది. సిలికాన్ ఆంధ్ర విశ్వవిద్యాలయం నుండి సర్టిఫైడ్ డాన్సర్‌గా, ఆమె కళ్యాణ శ్రీనివాసం వంటి బ్యాలెట్‌లలో ప్రధాన పాత్రలు పోషించింది.",
    "guru": "స్మత్. ప్రీతి తాంబోట్ల, పద్మశ్రీ డాక్టర్ శోభా నాయుడు శిష్యురాలిగా, కూచిపూడి నృత్యంలో విశిష్టత సాధించారు. రెండు గిన్నిస్ రికార్డులు సాధించిన ఆమె, భారత ప్రధాని నరేంద్ర మోడీ వంటి ప్రముఖుల ముందు ప్రదర్శన ఇచ్చారు. తన్మయి ఆర్ట్ స్టూడియో స్థాపించి కూచిపూడిని ప్రపంచవ్యాప్తంగా ప్రోత్సహిస్తున్నారు.",
    "achievements": "ప్రణవి విజయాలు అద్భుతం! స్ప్రింగ్ నెక్టార్ ఫౌండేషన్ అంతర్జాతీయ పోటీలో మొదటి బహుమతి, నృత్య విస్మయ టైటిల్, ఇండీవుడ్ టాలెంట్ హంట్‌లో బంగారు పతకం సాధించారు. కర్ణాటక సంగీతం మరియు సంస్కృతంలో కూడా ఆమె రాణించారు.",
    "event": "ఆగస్టు 2, 2025న సాయంత్రం 5:30 నుండి 9:30 వరకు హైదరాబాద్‌లోని రవీంద్ర భారతి ఆడిటోరియంలో ప్రణవి రంగప్రవేశానికి రండి. స్మత్. ప్రీతి తాంబోట్ల మార్గదర్శనంలో ఆమె కూచిపూడి ప్రదర్శనను చూడండి.",
    "invitation": "ఆగస్టు 2, 2025న హైదరాబాద్‌లోని రవీంద్ర భారతి ఆడిటోరియంలో శ్రీ ప్రణవి చింతలపూడి రంగప్రవేశానికి మీ సాంనిధ్యం కోరుతున్నాము. మీ హాజరు ఈ కళాత్మక ఉత్సవాన్ని మరపురానిదిగా చేస్తుంది. RSVP చేయండి.",
    "gallery": "ప్రణవి నృత్య ప్రయాణంలోని క్షణాలను గ్యాలరీలో చూడండి. ప్రాక్టీస్ సెషన్‌ల నుండి స్టేజ్ ప్రదర్శనల వరకు, ఈ చిత్రాలు ఆమె కూచిపూడి పట్ల అభిరుచిని సూచిస్తాయి.",
    "rsvp": "మీరు వస్తున్నారని మాకు తెలియజేయండి! ప్రణవి రంగప్రవేశానికి RSVP ఫారమ్‌ను పూరించండి మరియు ఈ ఆనందకర ఉత్సవంలో భాగం కండి."
}

# Generate audio for each section
for section, text in narration_content.items():
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="te-IN",
        name="te-IN-Wavenet-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    with open(f"audio/{section}.mp3", "wb") as out:
        out.write(response.audio_content)
    print(f"Generated audio/{section}.mp3")