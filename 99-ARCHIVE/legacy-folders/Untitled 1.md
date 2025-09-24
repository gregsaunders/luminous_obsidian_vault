<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environmental Monitoring Breakthrough - LinkedIn Slides</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            display: flex;
            gap: 30px;
            justify-content: center;
            flex-wrap: wrap;
            min-height: 100vh;
        }

        .slide {
            width: 600px;
            height: 700px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 8px 32px rgba(74, 144, 226, 0.15);
            padding: 50px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            position: relative;
            border: 1px solid rgba(74, 144, 226, 0.1);
        }

        .slide-number {
            position: absolute;
            top: 30px;
            right: 30px;
            background: linear-gradient(135deg, #4A90E2, #357ABD);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
        }

        h1 {
            color: #4A90E2;
            font-size: 32px;
            font-weight: 700;
            margin: 0 0 30px 0;
            line-height: 1.2;
            letter-spacing: -0.5px;
        }

        h2 {
            color: #4A90E2;
            font-size: 20px;
            font-weight: 600;
            margin: 20px 0 15px 0;
        }

        .intro-text {
            color: #444;
            font-size: 18px;
            margin-bottom: 25px;
            line-height: 1.4;
            font-weight: 400;
        }

        .choice-container {
            display: flex;
            gap: 20px;
            margin: 20px 0;
        }

        .choice-section {
            flex: 1;
            padding: 20px;
            border-radius: 8px;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            border-left: 5px solid #4A90E2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .choice-title {
            font-weight: 700;
            color: #4A90E2;
            margin-bottom: 12px;
            font-size: 16px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .choice-list {
            color: #555;
            font-size: 14px;
            line-height: 1.5;
            margin: 0;
            padding-left: 0;
            list-style: none;
        }

        .choice-list li {
            margin: 8px 0;
            padding-left: 15px;
            position: relative;
        }

        .choice-list li::before {
            content: "•";
            color: #4A90E2;
            font-weight: bold;
            position: absolute;
            left: 0;
        }

        .highlight-box {
            background: linear-gradient(135deg, #4A90E2, #357ABD);
            color: white;
            padding: 25px;
            border-radius: 12px;
            margin: 25px 0;
            text-align: center;
            font-weight: 600;
            font-size: 16px;
            line-height: 1.4;
            box-shadow: 0 6px 20px rgba(74, 144, 226, 0.25);
        }

        .question-header {
            color: #4A90E2;
            text-align: center;
            font-size: 22px;
            font-weight: 600;
            margin: 20px 0;
            line-height: 1.3;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #4A90E2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .benefits-intro {
            color: #444;
            font-weight: 400;
            margin: 20px 0 15px 0;
            font-size: 16px;
        }

        .benefits {
            margin: 20px 0;
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 20px;
            border-radius: 8px;
            border-left: 5px solid #4A90E2;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .benefit-item {
            display: flex;
            align-items: flex-start;
            margin: 15px 0;
            font-size: 15px;
        }

        .checkmark {
            color: #00A651;
            font-size: 18px;
            margin-right: 12px;
            font-weight: bold;
            margin-top: 2px;
        }

        .benefit-text {
            color: #333;
            font-weight: 600;
        }

        .benefit-subtext {
            color: #666;
            font-style: italic;
            font-size: 13px;
            margin-top: 4px;
            font-weight: 400;
        }

        .big-statement {
            background: linear-gradient(135deg, #4A90E2, #357ABD);
            color: white;
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            font-weight: 700;
            font-size: 18px;
            margin: 25px 0;
            line-height: 1.3;
            box-shadow: 0 6px 20px rgba(74, 144, 226, 0.25);
        }

        .era-text {
            text-align: center;
            margin: 18px 0;
            font-size: 17px;
            font-weight: 600;
            color: #4A90E2;
            line-height: 1.3;
        }

        .cta {
            margin-top: auto;
            text-align: center;
            padding-top: 30px;
            border-top: 3px solid #e9ecef;
        }

        .cta-title {
            color: #4A90E2;
            font-weight: 700;
            font-size: 18px;
            margin-bottom: 12px;
        }

        .cta-text {
            color: #555;
            font-size: 15px;
            margin-bottom: 15px;
            line-height: 1.4;
        }

        .website {
            color: #00A651;
            font-weight: 600;
            font-size: 16px;
        }

        .company-name {
            position: absolute;
            bottom: 30px;
            left: 30px;
            color: #4A90E2;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 0.5px;
        }
    </style>
</head>
<body>
    <!-- Slide 1 -->
    <div class="slide">
        <div class="slide-number">1</div>
        <h1>The 30-Year NA Monitoring Trap</h1>
        
        <p class="intro-text">For 30 years, oil sands environmental monitoring has been stuck in an impossible choice:</p>

        <div class="choice-container">
            <div class="choice-section">
                <div class="choice-title">⚡ FAST BUT CRUDE</div>
                <ul class="choice-list">
                    <li>Get rough estimates quickly</li>
                    <li>Miss critical compounds</li>
                    <li>Limited actionable data</li>
                </ul>
            </div>

            <div class="choice-section">
                <div class="choice-title">🔬 PRECISE BUT SLOW</div>
                <ul class="choice-list">
                    <li>Wait 2-8 weeks for HRMS results</li>
                    <li>Conditions change while waiting</li>
                    <li>Reactive instead of adaptive</li>
                </ul>
            </div>
        </div>

        <div class="highlight-box">
            This monitoring gap has held back adaptive environmental management across the industry.
        </div>

        <div class="company-name">LUMINOUS BIOSOLUTIONS</div>
    </div>

    <!-- Slide 2 -->
    <div class="slide">
        <div class="slide-number">2</div>
        <h1>The Game Changer</h1>
        
        <div class="intro-text">What if you could get quantitative naphthenic acid data in 24 hours?</div>

        <p class="benefits-intro">Our peer-reviewed biosensors deliver:</p>

        <div class="benefits">
            <div class="benefit-item">
                <span class="checkmark">✅</span>
                <div>
                    <div class="benefit-text">1.5-15 mg/L detection limits</div>
                    <div class="benefit-subtext">Regulatory-grade precision</div>
                </div>
            </div>

            <div class="benefit-item">
                <span class="checkmark">✅</span>
                <div>
                    <div class="benefit-text">24-hour turnaround</div>
                    <div class="benefit-subtext">Management-grade speed</div>
                </div>
            </div>

            <div class="benefit-item">
                <span class="checkmark">✅</span>
                <div>
                    <div class="benefit-text">Field-validated in real treatment systems</div>
                    <div class="benefit-subtext">Proven performance</div>
                </div>
            </div>
        </div>

        <div class="big-statement" style="margin: 20px 0 30px 0;">
            For the first time: PRECISION AND SPEED in environmental monitoring.
        </div>

        <div class="company-name">LUMINOUS BIOSOLUTIONS</div>
    </div>

    <!-- Slide 3 -->
    <div class="slide">
        <div class="slide-number">3</div>
        <h1>Why This Matters Now</h1>
        
        <p class="intro-text">Alberta's new monitoring requirements demand both rapid response AND analytical rigor.</p>

        <div class="big-statement">
            REAL-TIME ENVIRONMENTAL DATA = REAL-TIME ENVIRONMENTAL PROTECTION
        </div>

        <div class="era-text">The era of "monitor and hope" is ending.</div>
        <div class="era-text">The era of "monitor and adapt" is here.</div>

        <div class="cta">
            <div class="cta-title">Ready to close the monitoring gap?</div>
            <div class="cta-text">Let's discuss how rapid biosensing transforms environmental stewardship.</div>
            <div class="website">🌐 luminousbiosolutions.com</div>
        </div>

        <div class="company-name">LUMINOUS BIOSOLUTIONS</div>
    </div>
</body>
</html>
