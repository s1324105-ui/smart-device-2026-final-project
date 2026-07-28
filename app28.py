import streamlit as st
import random
import google.generativeai as genai
import json
from datetime import datetime

# APIキーは直接書かず、Streamlitのsecretsから取得するようにします
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("APIキーが st.secrets に見つかりません。ディレクトリ名が '.streamlit' (ドットあり) になっているか確認してください。")
    st.stop() # キーがない場合は処理を停止
model = genai.GenerativeModel("gemini-1.5-flash")

# ====== ここにあなたの questions_data をそのまま貼り付け ======
questions_data = {
    #6問
    "アメリカ": [

        {
            "question": "アメリカのレストランで一般的な習慣は？",

            "options": [
                "チップを渡す",
                "必ず靴を脱ぐ",
                "値段交渉する"
            ],

            "answer": "チップを渡す",

            "explanation":
            "アメリカではサービスへの感謝としてチップを渡す文化があります。",
            
            "category":"食文化"
        },


        {
            "question": "アメリカで会話をするとき大切にされることは？",

            "options": [
                "自分の意見を伝える",
                "何も話さない",
                "相手と必ず同じ意見にする",
                
            ],

            "answer":
            "自分の意見を伝える",

            "explanation":
            "自分の考えをはっきり伝えるコミュニケーションが重視されます。",
            
            "category":"会話"
        },


        {
            "question": "アメリカで初対面の人との挨拶として一般的なのは？",

            "options": [
                "握手",
                "深いお辞儀",
                "無言",
                
            ],

            "answer":
            "握手",

            "explanation":
            "握手は初対面やビジネスの場面でよく使われます。",
            
            "category":"マナー"
        },


        {
            "question": "アメリカでは時間についてどのように考えることが多い？",

            "options": [
                "時間を守ることを大切にする",
                "遅刻は必ず歓迎される",
                "時間は気にしない",
            ],

            "answer":
            "時間を守ることを大切にする",

            "explanation":
            "仕事や約束では時間を守ることが重要視されます。",
            
            "category":"生活"
        },


        {
            "question": "アメリカでプレゼントをもらった時の行動として一般的なのは？",

            "options": [
                "その場で感謝を伝える",
                "すぐ返す",
                "隠す"
            ],

            "answer":
            "その場で感謝を伝える",

            "explanation":
            "感謝を言葉で表現することが大切にされています。",
            
            "category":"マナー"
        },


        {
            "question": "アメリカの家庭でよく見られる食事スタイルは？",

            "options": [
                "家族で会話しながら食べる",
                "必ず無言で食べる",
                "立って食べる",
            ],

            "answer":
            "家族で会話しながら食べる",

            "explanation":
            "食事中の会話や交流を楽しむ文化があります。",
            
            "category":"食文化"
        }

    ],


#5問
    "韓国": [

        {
            "question":
            "韓国で年上の人を尊重する文化を何といいますか？",

            "options":[
                "儒教文化",
                "個人主義文化",
                "無関心文化",
            ],

            "answer":
            "儒教文化",

            "explanation":
            "韓国では年齢や上下関係を大切にする文化があります。",
            
            "category":"文化"
        },


        {
            "question":
            "韓国の伝統的な挨拶で使われるものは？",

            "options":[
                "お辞儀",
                "握手だけ",
                "手を振らない"
            ],

            "answer":
            "お辞儀",

            "explanation":
            "韓国では相手への敬意を表すためお辞儀をします。",
            
            "category":"マナー"
        },

    
    {
            "question":
            "韓国で「マナーが悪い」とされている行動は次のうちどれでしょうか？",

            "options":[
                "食事中にあぐらをかく",
                "食器を持ってご飯を食べる",
                "お酒を飲んでいる姿を隠す",
            ],

            "answer":
            "食器をもってご飯を食べる",

            "explanation":
            "韓国で 食事するときは食器は 置いたまま食べるのがマナーです。",
            
            "category":"マナー"
        },

        {
            "question":
            "韓国の学校ではいつから学校が始まる？",

            "options":[
                "4月",
                "3月",
                "8月",
            ],

            "answer":
            "3月",

            "explanation":
            "学期が始まるのは日本とはちがって３月から翌年の２月と、１カ月ずれています。そのうち12月末から2月までに長い冬休みがあります。夏休みは、7月末から8月末までのおよそ１カ月です。",
            
            "category":"生活"
        },

        {
            "question":
            "韓国で1番人気のスポーツは？",

            "options":[
                "サッカー",
                "テコンドー",
                "野球",
            ],

            "answer":
            "サッカー",

            "explanation":
            "プロリーグの「Kリーグ」があり、4年に１度行われるサッカーのワールドカップにも常連として出場している強豪です。",
            
            "category":"生活"
        },





     ],

     




#5問
    "フランス": [

        {
            "question":
            "フランスで食事はどのように考えられていますか？",

            "options":[
                "会話を楽しむ時間",
                "早く終わらせるもの",
                "一人だけの時間",
            ],

            "answer":
            "会話を楽しむ時間",

            "explanation":
            "食事は人との交流を楽しむ大切な時間です。",
            
            "category":"食文化"
        },
        {
            "question":
            "フランスの義務教育はいつから？",

            "options":[
                "3歳",
                "6歳",
                "10歳",
            ],

            "answer":
            "3歳",

            "explanation":
            "2019年度からは3才から16才までになりました。3才から5才までの3年間が幼稚園、6才からの5年間が小学校、4年間が中学校、その次の3年間（18才まで）が高校です。",
            
            "category":"生活"
        },

         {
            "question":
            "フランスにはフランス革命を祝う日があるが、フランス革命はいつ？",

            "options":[
                "7月1日",
                "7月4日",
                "7月14日",
            ],

            "answer":
            "7月14日",

            "explanation":
            "この日は「トリコロール（三色旗）」と呼よばれる国旗があちこちではためき、各地で花火が打ち上げられて盛大にお祝いをします。パリでは軍事パレードが行われ、大統領が演説するほか、各地で音楽祭やダンス・パーティーが行われます。ちなみに7月1日はカナダの独立記念日、7月4日はアメリカの独立記念日です。",
            
            "category":"生活"
        },
         {
            "question":
            "フランスでは買い物したくてもできない曜日がある。どの曜日？",

            "options":[
                "月曜日",
                "土曜日",
                "日曜日",
            ],

            "answer":
            "日曜日",

            "explanation":
            "カトリックの伝統が残るフランスでは、日曜日は安息日。スーパーマーケット、デパート、多くのお店が定休日となります。ですので買い物は土曜日までに済ますのが基本です。",
            
            "category":"生活"
        },

        {
            "question":
            "フランスでは世界で唯一認められているのがある。それは何？",

            "options":[
                "死後結婚",
                "未成年婚",
                "重婚",
            ],

            "answer":
            "死後結婚",

            "explanation":
            "フランスには、亡くなったパートナーと法的に結婚できる「死後結婚」という制度があります。もちろん無条件ではありません。「生前に結婚の意思が明確にあったこと（婚約していたなど）」や大統領の許可など、厳しい条件をクリアする必要があります",
            
            "category":"文化"
        },


    ],

    #5問
    "イギリス": [

        {
            "question":
            "フランスで食事はどのように考えられていますか？",

            "options":[
                "会話を楽しむ時間",
                "早く終わらせるもの",
                "一人だけの時間",
            ],

            "answer":
            "会話を楽しむ時間",

            "explanation":
            "食事は人との交流を楽しむ大切な時間です。",
            
            "category":"食文化"
        },
        {
            "question":
            "フランスの義務教育はいつから？",

            "options":[
                "3歳",
                "6歳",
                "10歳",
            ],

            "answer":
            "3歳",

            "explanation":
            "2019年度からは3才から16才までになりました。3才から5才までの3年間が幼稚園、6才からの5年間が小学校、4年間が中学校、その次の3年間（18才まで）が高校です。",
            
            "category":"生活"
        },

         {
            "question":
            "フランスにはフランス革命を祝う日があるが、フランス革命はいつ？",

            "options":[
                "7月1日",
                "7月4日",
                "7月14日",
            ],

            "answer":
            "7月14日",

            "explanation":
            "この日は「トリコロール（三色旗）」と呼よばれる国旗があちこちではためき、各地で花火が打ち上げられて盛大にお祝いをします。パリでは軍事パレードが行われ、大統領が演説するほか、各地で音楽祭やダンス・パーティーが行われます。ちなみに7月1日はカナダの独立記念日、7月4日はアメリカの独立記念日です。",
            
            "category":"生活"
        },
         {
            "question":
            "フランスでは買い物したくてもできない曜日がある。どの曜日？",

            "options":[
                "月曜日",
                "土曜日",
                "日曜日",
            ],

            "answer":
            "日曜日",

            "explanation":
            "カトリックの伝統が残るフランスでは、日曜日は安息日。スーパーマーケット、デパート、多くのお店が定休日となります。ですので買い物は土曜日までに済ますのが基本です。",
            
            "category":"生活"
        },

        {
            "question":
            "フランスでは世界で唯一認められているのがある。それは何？",

            "options":[
                "死後結婚",
                "未成年婚",
                "重婚",
            ],

            "answer":
            "死後結婚",

            "explanation":
            "フランスには、亡くなったパートナーと法的に結婚できる「死後結婚」という制度があります。もちろん無条件ではありません。「生前に結婚の意思が明確にあったこと（婚約していたなど）」や大統領の許可など、厳しい条件をクリアする必要があります",
            
            "category":"文化"
        },


    ],
    #5問
    "インド": [

        {
            "question":
            "インドで最も広く話されている公用語の一つはどれでしょう？",

            "options":[
                "タイ語",
                "インド語",
                "ヒンドゥー語",
            ],

            "answer":
            "ヒンドゥー語",

            "explanation":
            "ヒンディー語はインドで最も広く使われている言語の一つです。ただし、インドには22の公認言語があり、地域によってベンガル語やタミル語などさまざまな言語が話されています。",
            
            "category":"生活"
        },
        {
            "question":
            "インドの女性が伝統的な場で着ることが多い衣装はどれでしょう？",

            "options":[
                "チマ・チョゴリ",
                "サリー",
                "アオザイ",
            ],

            "answer":
            "サリー",

            "explanation":
            "サリーは長い布を体に巻き付けて着るインドの伝統衣装です。色や柄が豊富で、結婚式やお祭りなど特別な日に着ることもあります。",
            
            "category":"生活"
        },

         {
            "question":
            "インドで「光の祭り」として知られるお祭りはどれでしょう？",

            "options":[
                "ディーワーリー",
                "オクトーバーフェスト",
                "ハロウィン",
            ],

            "answer":
            "ディーワーリー",

            "explanation":
            "ディーワーリーはインド最大級のお祭りで、家や町をたくさんのランプや光で飾ります。光が闇に打ち勝つことを祝うお祭りとして親しまれています。",
            
            "category":"文化の違い"
        },
         {
            "question":
            "インド発祥とされるスポーツはどれでしょう？",

            "options":[
                "クリケット",
                "カバディ",
                "野球",
            ],

            "answer":
            "カバディ",

            "explanation":
            "カバディはインド発祥とされる伝統的なスポーツです。相手チームにタッチして戻る競技で、呼吸を止めずに「カバディ」と言い続けるルールが特徴です。",
            
            "category":"生活"
        },

        {
            "question":
            "インドの国旗の中央に描かれている青い模様は何でしょう？",

            "options":[
                "アショーカ・チャクラ（法輪）",
                "ライオン",
                "花",
            ],

            "answer":
            "アショーカ・チャクラ（法輪）",

            "explanation":
            "アショーカ・チャクラは24本のスポーク（線）を持つ青い車輪です。正義や進歩、平和などを表すシンボルとして国旗の中央に描かれています。",
            
            "category":"宗教"
        },


    ],
    #5問
    "中国": [

        {
            "question":
            "中国の旧正月を何と呼ぶでしょう？",

            "options":[
                "春節",
                "中秋節",
                "端午節",
            ],

            "answer":
            "春節",

            "explanation":
            "春節は中国で最も大切な祝日の一つです。家族が集まり、ごちそうを食べたり、お年玉を渡したりして新年を祝います。",
            
            "category":"生活"
        },
        {
            "question":
            "日本と中国で食事の文化が異なる点として正しいものはどれでしょう？",

            "options":[
                "中国では料理を大皿で取り分けて食べることが多い",
                "中国では食事中に飲み物は禁止されている",
                "中国では一人ずつ決まった料理しか食べない",
            ],

            "answer":
            "中国では料理を大皿で取り分けて食べることが多い",

            "explanation":
            "中国では家族や友人と大皿料理を囲み、取り分けて食べる文化が一般的です。日本では一人分ずつ盛り付けられることが比較的多いです。",
            
            "category":"食事"
        },

         {
            "question":
            "中国で多くの人が使っているコミュニケーションアプリはどれでしょう？",

            "options":[
                "LINE",
                "WeChat",
                "mail",
            ],

            "answer":
            "WeChat",

            "explanation":
            "WeChat（微信）はメッセージのやり取りだけでなく、決済や買い物、予約などにも利用される便利なアプリです。",
            
            "category":"生活"
        },
         {
            "question":
            "中国で家族や友人へのお土産として避けられることがある物はどれでしょう？",

            "options":[
                "お茶",
                "お菓子",
                "時計",
            ],

            "answer":
            "時計",

            "explanation":
            "中国では「時計を贈る」という言葉の響きが「葬儀に参列する」という言葉に似ているため、縁起がよくないと考える人もいます。",
            
            "category":"生活"
        },

        {
            "question":
            "中国の多くの飲食店で無料で提供されることがある飲み物はどれでしょう？",

            "options":[
                "温かいお茶",
                "ラッシー",
                "コーヒー",
            ],

            "answer":
            "温かいお茶",

            "explanation":
            "中国では食事の際に温かいお茶が無料で提供されるお店が多くあります。冷たい水ではなく、お茶が出されることも珍しくありません。",
            
            "category":"生活"
        },


    ],
    #5問
    "ブラジル": [

    {
        "question":
        "ブラジルの主食としてよく食べられている組み合わせは？",

        "options":[
            "米と豆",
            "パンとチーズ",
            "麺と茄子"
        ],

        "answer":
        "米と豆",

        "explanation":
        "ブラジルでは『米と豆』が毎日の食卓によく並びます。肉やサラダと一緒に食べる家庭も多く、栄養バランスのよい食事として親しまれています。",

        "category":"食事"
    },

    {
        "question":
        "ブラジルで人と会ったときのあいさつとして一般的なのは？",

        "options":[
            "笑顔で握手やあいさつをする",
            "深くお辞儀をする",
            "頭をぶつける"
        ],

        "answer":
        "笑顔で握手やあいさつをする",

        "explanation":
        "ブラジルでは笑顔で握手をしたり、『Olá（オラ）』とあいさつをしたりすることが一般的です。親しい人同士ではハグや頬へのキスをすることもあります。",

        "category":"あいさつ"
    },

    {
        "question":
        "ブラジルでは学校生活でどのような服装が多いでしょう？",

        "options":[
            "制服を着る学校が多い",
            "カーニバル衣装",
            "私服で通学する"
        ],

        "answer":
        "制服を着る学校が多い",

        "explanation":
        "ブラジルでは公立・私立を問わず制服を採用している学校が多く見られます。",

        "category":"生活"
    },

    {
        "question":
        "ブラジルで多くの家庭が楽しむスポーツはどれでしょう？",

        "options":[
            "相撲",
            "サッカー",
            "アイスホッケー"
        ],

        "answer":
        "サッカー",

        "explanation":
        "ブラジルではサッカーが国民的人気スポーツで、公園や学校などでも気軽に楽しまれています。",

        "category":"交通"
    },

    {
        "question":
        "ブラジルで毎年開かれる世界的に有名なお祭りは？",

        "options":[
            "リオのカーニバル",
            "ねぶた祭",
            "祇園祭"
        ],

        "answer":
        "リオのカーニバル",

        "explanation":
        "リオデジャネイロで開催される『リオのカーニバル』は、世界最大級のお祭りとして有名で、多くの観光客が訪れます。",

        "category":"生活"
    }

   ],
    #5問
    "スペイン": [

    {
        "question":
        "スペインでは昼食後に多くの店が一時的に閉まる習慣があります。この時間帯を何といいますか？",

        "options":[
            "シエスタ",
            "フィエスタ",
            "マニャーナ"
        ],

        "answer":
        "シエスタ",

        "explanation":
        "シエスタは昼食後に休憩をとる習慣です。現在では都市部では減っていますが、地方では今でも見られます。",

        "category":"生活"
    },

    {
        "question":
        "スペイン料理『パエリア』の発祥地として知られている地域はどこでしょう？",

        "options":[
            "バレンシア地方",
            "カタルーニャ地方",
            "アンダルシア地方"
        ],

        "answer":
        "バレンシア地方",

        "explanation":
        "パエリアはスペイン東部のバレンシア地方で生まれた料理です。本場では魚介だけでなく、鶏肉やうさぎ肉を使うこともあります。",

        "category":"食事"
    },

    {
        "question":
        "日本とスペインの文化の違いとして正しいものはどれでしょう？",

        "options":[
            "夕食の時間が日本より遅いことが多い",
            "毎日午後5時までに夕食を食べる",
            "夕食では会話をしないことが一般的である"
        ],

        "answer":
        "夕食の時間が日本より遅いことが多い",

        "explanation":
        "スペインでは夕食が午後9時以降になる家庭も多く、日本より食事の時間が遅いことが特徴です。",

        "category":"文化の違い"
    },

    {
        "question":
        "スペインで毎年7月に開催される『牛追い祭り』で有名な都市はどこでしょう？",

        "options":[
            "パンプローナ",
            "マドリード",
            "セビリア"
        ],

        "answer":
        "パンプローナ",

        "explanation":
        "パンプローナで開催される『サン・フェルミン祭』では、牛追い（エンシエロ）が世界的に有名です。",

        "category":"文化の違い"
    },

    {
        "question":
        "スペインではサッカー以外にも人気の高いスポーツがあります。それは次のうちどれでしょう？",

        "options":[
            "バスケットボール",
            "相撲",
            "ラクロス"
        ],

        "answer":
        "バスケットボール",

        "explanation":
        "スペインではサッカーが最も人気ですが、バスケットボールも非常に盛んで、国際大会でも強豪国として知られています。",

        "category":"生活"
    }

],
    #5問
    "ドイツ": [

    {
        "question":
        "ドイツで日曜日に多くのスーパーマーケットや商店が閉まる理由として最も適切なのは？",

        "options":[
            "労働者の休日を大切にする法律や文化があるため",
            "毎週全国でイベントが開催されるため",
            "日曜日は電気が止まるため"
        ],

        "answer":
        "労働者の休日を大切にする法律や文化があるため",

        "explanation":
        "ドイツでは『日曜日は休息の日』という考えがあり、多くの商店が営業していません。買い物は土曜日までに済ませる人が多いです。",

        "category":"生活"
    },

    {
        "question":
        "ドイツ料理『ザワークラウト』とは、どのような食べ物でしょう？",

        "options":[
            "発酵させたキャベツ",
            "ジャガイモのスープ",
            "ソーセージをパンで挟んだ料理"
        ],

        "answer":
        "発酵させたキャベツ",

        "explanation":
        "ザワークラウトはキャベツを乳酸発酵させた保存食で、ソーセージや肉料理の付け合わせとしてよく食べられています。",

        "category":"食事"
    },

    {
        "question":
        "日本とドイツの文化の違いとして正しいものはどれでしょう？",

        "options":[
            "ドイツでは環境保護やごみの分別が非常に重視されている",
            "ドイツではごみを分別しないことが一般的である",
            "ドイツでは家庭から出るごみはすべて無料で回収される"
        ],

        "answer":
        "ドイツでは環境保護やごみの分別が非常に重視されている",

        "explanation":
        "ドイツでは環境保護への意識が高く、ごみの分別方法も細かく決められています。リサイクルを重視する文化が根付いています。",

        "category":"文化の違い"
    },

    {
        "question":
        "ドイツの世界的なお祭り『オクトーバーフェスト』は、主にどの都市で開催されるでしょう？",

        "options":[
            "ミュンヘン",
            "ベルリン",
            "ハンブルク"
        ],

        "answer":
        "ミュンヘン",

        "explanation":
        "オクトーバーフェストはミュンヘンで開催される世界最大級の祭りで、多くの観光客が訪れます。",

        "category":"文化の違い"
    },

    {
        "question":
        "ドイツでは高速道路『アウトバーン』が有名です。その特徴として正しいものはどれでしょう？",

        "options":[
            "一部区間では法定速度の上限が設定されていない",
            "すべての区間で時速50kmまでしか出せない",
            "一般車は走行できない"
        ],

        "answer":
        "一部区間では法定速度の上限が設定されていない",

        "explanation":
        "アウトバーンには速度制限のない区間がありますが、すべての道路ではなく、安全のため推奨速度や制限速度が設定されている区間も多くあります。",

        "category":"生活"
    }

],
    #5問
    "スウェーデン": [

    {
        "question":
        "スウェーデンで多くの人が仕事や学校の合間に楽しむコーヒー休憩の習慣を何といいますか？",

        "options":[
            "フィーカ",
            "シエスタ",
            "ブランチ"
        ],

        "answer":
        "フィーカ",

        "explanation":
        "フィーカはコーヒーやお菓子を楽しみながら家族や友人、同僚と会話をするスウェーデン独特の習慣です。単なる休憩ではなく、人との交流を大切にする文化として親しまれています。",

        "category":"生活"
    },

    {
        "question":
        "スウェーデン料理『スールストレミング』は、どのような食べ物でしょう？",

        "options":[
            "発酵させたニシン",
            "甘いシナモンパン",
            "トナカイのシチュー"
        ],

        "answer":
        "発酵させたニシン",

        "explanation":
        "スールストレミングは発酵させたニシンを缶詰にした伝統料理で、独特の強い香りが特徴です。",

        "category":"食文化"
    },

    {
        "question":
        "日本とスウェーデンの文化の違いとして正しいものはどれでしょう？",

        "options":[
            "スウェーデンでは仕事と私生活のバランスを重視する考え方が広く浸透している",
            "スウェーデンでは休日に働くことが最も評価される",
            "スウェーデンでは家族より仕事を優先することが一般的である"
        ],

        "answer":
        "スウェーデンでは仕事と私生活のバランスを重視する考え方が広く浸透している",

        "explanation":
        "スウェーデンでは『ワークライフバランス』を大切にする文化が根付いており、家族との時間や休暇を重視する人が多いことが特徴です。",

        "category":"文化の違い"
    },

    {
        "question":
        "スウェーデンでは環境保護のために家庭で行われていることとして一般的なのはどれでしょう？",

        "options":[
            "細かくごみを分別してリサイクルする",
            "家庭ごみはすべて一つの袋に入れる",
            "ペットボトルは回収しない"
        ],

        "answer":
        "細かくごみを分別してリサイクルする",

        "explanation":
        "スウェーデンは環境先進国として知られ、ごみの分別やリサイクルが徹底されています。飲料容器にはデポジット制度も導入されています。",

        "category":"生活"
    },

    {
        "question":
        "スウェーデンで毎年12月13日に行われる、白い衣装とろうそくの冠で知られる伝統行事は何でしょう？",

        "options":[
            "ルシア祭",
            "ミッドサマー祭",
            "イースター祭"
        ],

        "answer":
        "ルシア祭",

        "explanation":
        "ルシア祭は光の聖人ルシアをたたえる伝統行事です。白い衣装を着た人々が歌を歌いながら行進し、冬の訪れを彩るスウェーデンを代表する文化の一つです。",

        "category":"文化"
    }

],


}

def generate_ai_question(country,level):
    prompt = f"""
あなたは異文化教育の先生です。

国：{country}
難易度：{level}

難易度に応じて旅行者向けの4択クイズを1問作ってください。

初級
・あいさつ
・自己紹介
・学校
・生活

中級
・食事
・買い物
・交通
・ホテル

上級
・宗教
・ビジネス
・価値観
・文化の違い

JSONのみ出力してください。

{{
"question":"",
"options":["","","",""],
"answer":"",
"explanation":"",
"category":""
}}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # ```json を削除
    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    return json.loads(text)
# ============================================================

for k,v in {
    "questions":[],
    "answers":[],
    "number":0,
    "finish":False,
    "answered":False,
    "last_correct":False,
    "history":[],
    "ai_evaluation": None,
    "saved": False
}.items():
    if k not in st.session_state:
        st.session_state[k]=v

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #D7F3FF, #FFFFFF);
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 AI世界文化教師")

st.subheader("🌏 学びたい国を選んでください")

if "country" not in st.session_state:
    st.session_state.country = None

countries = [
    ("アメリカ", "usa.png"),
    ("韓国", "korea.png"),
    ("フランス", "france.png"),
    ("イギリス", "uk.png"),
    ("インド", "india.png"),
    ("中国", "china.png"),
    ("ブラジル", "brazil.png"),
    ("スペイン", "spain.png"),
    ("ドイツ", "germany.png"),
    ("スウェーデン", "sweden.png")
]

cols = st.columns(3)

for i, (name, img) in enumerate(countries):

    with cols[i % 3]:

        # 選択中なら緑色のカード
        if st.session_state.country == name:
            st.success("✅ 選択中")

        st.image(img, use_container_width=True)

        if st.button(
            f"🌏 {name}",
            key=name,
            use_container_width=True,
            type="primary" if st.session_state.country == name else "secondary"
        ):
            st.session_state.country = name
            st.rerun()

# 下に選択中の国を表示
if st.session_state.country:
    st.success(f"🌏 選択中：{st.session_state.country}")

level = st.radio(
    "🎓 難易度を選択",
    ["初級", "中級", "上級"],
    horizontal=True
)

# 難易度の説明
if level == "初級":
    st.info("""
🌱 **初級**

・あいさつ
・自己紹介
・学校
・生活
""")

elif level == "中級":
    st.info("""
🍽️ **中級**

・食事
・買い物
・交通
・ホテル
""")

else:
    st.info("""
🏛️ **上級**

・宗教
・ビジネスマナー
・価値観
・文化の違い
""")

if st.button("🚀 スタート") and st.session_state.country:

    fixed_questions = random.sample(
    questions_data[st.session_state.country],
    5)
    st.session_state.questions = fixed_questions
    st.session_state.answers = []
    st.session_state.number = 0
    st.session_state.finish = False
    st.session_state.answered = False
    st.session_state.ai_evaluation = None
    st.session_state.saved = False

    st.rerun()

if st.session_state.questions and not st.session_state.finish:
    q=st.session_state.questions[st.session_state.number]
    st.subheader(f"問題 {st.session_state.number+1}/5")
    st.write(q["question"])
    choice=st.radio("答え",q["options"],key=f"q{st.session_state.number}")

    if not st.session_state.answered:
        if st.button("回答"):
            ok=choice==q["answer"]
            st.session_state.answers.append({
                "question":q["question"],
                "your_answer":choice,
                "correct_answer":q["answer"],
                "correct":ok,
                "category":q["category"]
            })
            st.session_state.last_correct=ok
            st.session_state.answered=True
            st.rerun()
    else:
        if st.session_state.last_correct:
            st.success("⭕ 正解")
        else:
            st.error("❌ 不正解")
        st.write("### あなたの回答")
        st.write(st.session_state.answers[-1]["your_answer"])
        st.write("### 正解")
        st.write(q["answer"])
        st.info(q["explanation"])

        if st.button("次の問題へ"):
            st.session_state.answered=False
            if st.session_state.number<4:
                st.session_state.number+=1
            else:
                st.session_state.finish=True
            st.rerun()

if st.session_state.finish:
    score=sum(a["correct"] for a in st.session_state.answers)
    # ===== 履歴保存 =====
    if not st.session_state.saved:
        st.session_state.history.append({
            "date": datetime.now().strftime("%Y/%m/%d %H:%M"),
            "country": st.session_state.country,
            "level": level,
            "score": score,
            "answers": st.session_state.answers.copy()
        })
        st.session_state.saved = True
    st.header("🎉 結果")
    st.write(f"## 正解数：{score}/5")

    for i,a in enumerate(st.session_state.answers,1):
        st.write(f"### 問題{i}")
        st.write(a["question"])
        st.write(f"あなたの回答：{a['your_answer']}")
        st.write(f"正解：{a['correct_answer']}")
        st.write("⭕" if a["correct"] else "❌")
        st.divider()

    prompt=f'''
あなたは世界文化の先生です。
国:{ st.session_state.country}
難易度:{level}
結果:{st.session_state.answers}
正解数:{score}/5

以下を日本語で出力してください。
・文化理解度(100点)
・星5段階評価
・苦手な分野

'''
    st.header("🤖 AI評価")
    
    # AI評価がまだ生成されていない場合のみAPIを呼び出す
    if st.session_state.ai_evaluation is None:
        with st.spinner("AI先生が評価を生成中..."):
            try:
                response = model.generate_content(prompt)
                if response and response.text:
                    st.session_state.ai_evaluation = response.text
                else:
                    st.session_state.ai_evaluation = "AIからの回答が空でした。もう一度お試しください。"
            except Exception as e:
                st.error("AI評価の生成中にエラーが発生しました。")
                st.session_state.ai_evaluation = "評価を取得できませんでした。"

    st.write(st.session_state.ai_evaluation)

    # 最初に戻るボタン
    if st.button("🏠 最初に戻って別の国を学ぶ"):
        st.session_state.questions = []
        st.session_state.finish = False
        st.session_state.country = None
        st.session_state.ai_evaluation = None
        st.rerun()

st.divider()
st.header("📚 学習履歴")

if len(st.session_state.history) == 0:
    st.info("まだ履歴はありません。")
else:
    for i, h in enumerate(reversed(st.session_state.history), 1):

        with st.expander(
            f"{i}. {h['date']}  {h['country']}（{h['level']}） {h['score']}/5"
        ):

            for j, ans in enumerate(h["answers"], 1):
                st.write(f"### 問題{j}")
                st.write(ans["question"])
                st.write(f"あなた：{ans['your_answer']}")
                st.write(f"正解：{ans['correct_answer']}")
                st.write("⭕ 正解" if ans["correct"] else "❌ 不正解")
                st.divider()
