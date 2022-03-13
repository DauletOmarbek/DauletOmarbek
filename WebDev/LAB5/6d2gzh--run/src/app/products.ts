export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

export const products = [
  {
    id: 1,
    imge: 'https://m.media-amazon.com/images/I/81bc8mA3nKL._AC_SL1500_.jpg',
    name: 'Acer Nitro 5',
    price: 1355,
    description: 'Dominate the Game: Great performance meets long battery life with the Intel Core i7-11800H Processor - up to 4.6GHz, 8 cores, 16 threads, 24MB Intel Smart Cache',
    link: 'https://www.amazon.com/Acer-AN515-55-53E5-i5-10300H-GeForce-Keyboard/dp/B092YHJGMN/ref=sr_1_1?crid=3BGOUPQI4SZL2&keywords=Acer+Nitro+5&qid=1647096187&sprefix=acer+nitro+5%2Caps%2C389&sr=8-1'
  },
  {
    id: 2,
    imge: 'https://m.media-amazon.com/images/I/415G0bg-hiL._AC_SL1000_.jpg',
    name: 'Samsung Galaxy Tab S6 Lite 10.4',
    price: 300,
    description: 'S PEN INCLUDED: The included S Pen makes it easier than ever to write notes and personalize photos and videos, all without needing to charge. The S Pen attaches magnetically right to your tablet and is always ready to go.',
    link: 'https://www.amazon.com/Samsung-Galaxy-Lite-Tablet-Angora/dp/B086Z3S3MY/ref=sr_1_3?crid=Y2TTRFYKGRDB&keywords=Samsung+Galaxy+Tab+S6+Lite+10.4&qid=1647096238&sprefix=samsung+galaxy+tab+s6+lite+10.4%2Caps%2C260&sr=8-3'
  },
  {
    id: 3,
    imge: 'https://m.media-amazon.com/images/I/91UsHjAPTlL._AC_SL1500_.jpg',
    name: 'SAMSUNG 32-inch Class LED Smart FHD TV 1080P',
    price: 299,
    description: '',
    link: 'https://www.amazon.com/Samsung-Electronics-UN32N5300AFXZA-1080p-Smart/dp/B07CL4GLQW/ref=sr_1_3?crid=29FU1SIIQC1Y6&keywords=SAMSUNG+32-inch+Class+LED+Smart+FHD+TV+1080P&qid=1647096291&sprefix=samsung+32-inch+class+led+smart+fhd+tv+1080p%2Caps%2C251&sr=8-3'
  },
  {
    id: 4,
    imge: 'https://m.media-amazon.com/images/I/715-ylQIhsL._AC_SL1500_.jpg',
    name: 'Epson VS260 3-Chip 3LCD XGA Projector',
    price: 180,
    description: 'Amazing brightness — 3,300 lumens of color and white brightness (1) ideal for displaying large-group presentations, spreadsheets and videos, even in well-lit rooms',
    link: 'https://www.amazon.com/Epson-3-Chip-Projector-Brightness-Speaker/dp/B08L7KHB5J/ref=sr_1_3?crid=8GQPMRT4LFPU&keywords=Epson+VS260+3-Chip+3LCD+XGA+Projector&qid=1647096335&sprefix=epson+vs260+3-chip+3lcd+xga+projector%2Caps%2C248&sr=8-3'
  },
  {
    id: 5,
    imge: 'https://m.media-amazon.com/images/I/8167Vk47NGL._AC_SL1500_.jpg',
    name: 'GoPro HERO9 Black',
    price: 140,
    description: '5K VIDEO: Shoot stunning video with up to 5K resolution, perfect for maintaining serious detail even when zooming in. Packing a new 23.6MP sensor that’s an absolute powerhouse, HERO9 Black brings lifelike image sharpness, fluid motion and in-camera horizon leveling that always impresses.',
    link: 'https://www.amazon.com/GoPro-HERO9-Black-Commerce-Stabilization/dp/B09J713ZS7/ref=sr_1_1_sspa?crid=VIGX3FVDJJ50&keywords=GoPro+HERO9+Black&qid=1647096380&sprefix=gopro+hero9+black%2Caps%2C340&sr=8-1-spons&psc=1&smid=ANIVUW1SREVVT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyWktBTU5ITDVFR0dLJmVuY3J5cHRlZElkPUEwNjA2ODgyMkk4N0lEUDNXQTREVCZlbmNyeXB0ZWRBZElkPUEwODQ3NDM3RFgzU1hJRkRRS0hZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
  },
  {
    id: 6,
    imge: 'https://m.media-amazon.com/images/I/719p0eyZiSL._AC_SL1500_.jpg',
    name: 'SAMSUNG Galaxy Buds Pro',
    price: 117,
    description: 'Intelligent Active Noise Cancellation: Escape and tune in to your own moment of Zen — all with a single tap; Answer calls and instantly switch to talking with voice detection and let in the sounds that matter most with 4 ambient levels',
    link: 'https://www.amazon.com/Bluetooth-Wireless-Cancelling-Charging-Resistant/dp/B08MWZHHKP/ref=sr_1_3?crid=1RKWRXIHSIBFJ&keywords=SAMSUNG+Galaxy+Buds+Pro&qid=1647096413&sprefix=samsung+galaxy+buds+pro%2Caps%2C250&sr=8-3'
  },
  {
    id: 7,
    imge: 'https://m.media-amazon.com/images/I/71FuI8YvCNL._AC_SL1500_.jpg',
    name: 'Apple iPhone 12 Pro Max, 256GB',
    price: 500,
    description: 'Unlocked and compatible with any carrier of choice on GSM and CDMA networks (e.g. AT&T, T-Mobile, Sprint, Verizon, US Cellular, Cricket, Metro, Tracfone, Mint Mobile, etc.).',
    link: 'https://www.amazon.com/Apple-iPhone-12-Pro-Max/dp/B09JFFG8D7/ref=sr_1_1?crid=2JABPDY281PH1&keywords=Apple+iPhone+12+Pro+Max%2C+256GB&qid=1647096440&sprefix=apple+iphone+12+pro+max%2C+256gb%2Caps%2C247&sr=8-1'
  },
  {
    id: 8,
    imge: 'https://m.media-amazon.com/images/I/61fEy55xUeL._AC_SL1500_.jpg',
    name: 'SAMSUNG Galaxy Z Flip 3 5G',
    price: 700,
    description: 'Flex Your Best Angle: With Flex Mode, Just Unfold Your Mobile Phone’S Screen To Your Best Angle For Hands-Free Pics And Video Calls; Choose What You Want To Capture, Set It Down, Stand Back And Shoot Your Best Shot',
    link: 'https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Intuitive-Warranty/dp/B097CMVWN9/ref=sr_1_3?crid=2G2JDBM8710O9&keywords=SAMSUNG+Galaxy+Z+Flip+3+5G&qid=1647096469&sprefix=samsung+galaxy+z+flip+3+5g%2Caps%2C564&sr=8-3'
  },
  {
    id: 9,
    imge: 'https://m.media-amazon.com/images/I/61yjoRgptdL._AC_SL1500_.jpg',
    name: 'JBL Tune 510BT',
    price: 45,
    description: 'The Tune 510BT wireless headphones feature renowned JBL Pure Bass sound, which can be found in the most famous venues all around the world.',
    link: 'https://www.amazon.com/JBL-Tune-710BT-Wireless-Headphones/dp/B095QN9WHH/ref=sr_1_6?crid=DOXFN36MTSAI&keywords=JBL+Tune+510BT&qid=1647096496&sprefix=jbl+tune+510bt%2Caps%2C250&sr=8-6'
  },
  {
    id: 10,
    imge: 'https://m.media-amazon.com/images/I/71trhuzbhML._AC_SL1500_.jpg',
    name: 'HP VH240a 23.8-Inch Full HD',
    price: 220,
    description: 'RESOLUTION & PANEL — 23.8-inch Full HD monitor (1920 x 1080p at 60 Hz) with 16:9 aspect ratio and an anti-glare matte IPS LED-backlit panel (2 million pixels, 16.7 million colors)',
    link: 'https://www.amazon.com/HP-23-8-inch-Adjustment-Speakers-VH240a/dp/B072M34RQC/ref=sr_1_1?crid=1BAXTEVOQZ8MM&keywords=HP+VH240a+23.8-Inch+Full+HD&qid=1647096540&sprefix=hp+vh240a+23.8-inch+full+hd%2Caps%2C249&sr=8-1'
  },
];


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/