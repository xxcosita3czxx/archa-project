/*const artForms = [
    { name: 'visuální umění', icon: '🎨', color: '#FF9AA2' },
    { name: 'hudební', icon: '🎵', color: '#FFB7B2' },
    { name: 'divadelní', icon: '🎭', color: '#FFDAC1' },
    { name: 'taneční', icon: '💃', color: '#E2F0CB' },
];

const challenges = {
    'visuální umění': [
        "Rekonstruj slavný obraz pouze pomocí emotikonů",
        "Nakresli autoportrét nedominantní rukou.",
        "Vytvoř koláž představující váš týden pouze pomocí výstřižků z časopisů.",
    ],
    'hudební': [
        "Slož 30 sekundovou znělku pro tvoji oblíbenou svačinu",
        "Vytvoř remix zvuku tvého budíku",
        "Slož básničku o tvém snu",
    ],
    'divadelní': [
        "Předveď minutový monolog v roli své oblíbené filmové postavy.",
        "Zahraj scénu ze svého dne, ale ve stylu němého filmu.",
        "Improvizuj reklamu na směšný produkt",
    ],
    'taneční': [
        "Choreografuj 15sekundového tance na oblíbenou meme píseň",
        "Vytvoř TikTok tanec napsaný nějakým AI",
        "Vytvoř taneční pohyb inspirovaný vaším domácím mazlíčkem nebo oblíbeným zvířetem.",
    ],
};

const wheel = document.getElementById('wheel');
const spinButton = document.getElementById('spinButton');
const challengeContainer = document.getElementById('challengeContainer');
const challengeText = document.getElementById('challengeText');
const challenge = document.getElementById('challenge');

let spinning = false;

spinButton.addEventListener('click', spinWheel);

let currentRotation = 0;  // Keep track of the current rotation

function spinWheel() {
    if (spinning) return;
    spinning = true;

    // Generate a random degree between 720 and 1080 (2-3 full rotations)
    const randomDegree = Math.floor(Math.random() * 360) + 720;
    
    // Add the random degree to the current rotation
    currentRotation += randomDegree;
    
    // Apply the rotation to the wheel
    wheel.style.transform = `rotate(${currentRotation}deg)`;

    setTimeout(() => {
        spinning = false;

        // Calculate the final rotation within the 360-degree range
        let finalRotation = currentRotation % 360;


        while (finalRotation > 360) {
            finalRotation -= 360;
        }

        // Check the final angle with multiple if conditions
        let selectedArt;

        if (finalRotation < 90) {
            selectedArt = artForms.find(art => art.name === 'hudební'); // Music
        } 
        
        if (finalRotation >= 90 && finalRotation < 180) {
            selectedArt = artForms.find(art => art.name === 'visuální umění'); // Visual Art
        } 
        
        if (finalRotation >= 180 && finalRotation < 270) {
            selectedArt = artForms.find(art => art.name === 'taneční'); // Theater
        } 
        
        if (finalRotation >= 270 && finalRotation < 360) {
            selectedArt = artForms.find(art => art.name === 'divadelní'); // Dance
        }

        // Display the selected challenge
        displayChallenge(selectedArt);
    }, 3000);  // Duration of the spin
}function displayChallenge(artForm) {
    const artChallenges = challenges[artForm.name];
    const randomChallenge = artChallenges[Math.floor(Math.random() * artChallenges.length)];
    
    challengeText.textContent = `Tvoje ${artForm.name} Challenge:`;
    challenge.textContent = randomChallenge;
    challengeContainer.style.display = 'block';
}*/