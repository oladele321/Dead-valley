System.Collections;
using System.Collections.Generic;
using UnityEngine; 
using UnityEngine.UI; 
public class GameDirector : MonoBehaviour 
{ 
    [Header("--- CONCEPT 2: NIGHT SHIFT CHORES ---")] 
    public int totalChores = 5; 
    private int completedChores = 0; 
    public List<GameObject> anomalyObjects; // Assign props that will move/disappear 
    [Header("--- CONCEPT 3: FAKE CHAT SYSTEM ---")] 
    public Text chatTextWindow; // Assign your UI Text/TextMeshPro 
    public ScrollRect chatScrollRect; 
    private List<string> chatMessages = new List<string>(); 
    private string[] chatPool = { 
        "Streamer look behind you!!", 
        "Wait, did that door just open?", 
        "LMAO he doesn't see the anomaly", 
        "W777777777777", 
        "Is that a person standing in the hallway??", 
        "CHECK THE CAMERAS NOW", 
        "Fake, it's just a jump scare game", 
        "BRO RUN SHE IS RIGHT THERE"
    }; 
    [Header("--- CONCEPT 4: BODYCAM & MONSTER ---")] 
    public Material bodycamShaderMaterial; // Assign your fish-eye/glitch post-processing material
    public Transform playerTransform;
    public Transform monsterTransform;
    public float monsterJumpscareDistance = 2.0f;
    public float monsterWarningDistance = 10.0f;
    
    private bool isGameOver = false;
    
     void Start()
      { // Start the background systems StartCoroutine(SimulateFakeChat());
           StartCoroutine(TriggerRandomAnomalies());
            if (bodycamShaderMaterial != null)
             bodycamShaderMaterial.SetFloat("_GlitchIntensity", 0.0f);
              } 
              void Update() { if (isGameOver) return; HandleMonsterProximity(); HandlePlayerInputs(); } // ========================================== // CONCEPT 2: CHORE & ANOMALY SYSTEM // ========================================== public void CompleteChore() { completedChores++; AddChatMessage("SYSTEM", $"Chore completed ({completedChores}/{totalChores})"); if (completedChores >= totalChores) TriggerWinCondition(); } IEnumerator TriggerRandomAnomalies() { while (!isGameOver) { yield return new WaitForSeconds(Random.Range(15f, 30f)); if (anomalyObjects.Count > 0) { // Pick a random object and mess with it (e.g., tip it over or hide it) GameObject targetAnomaly = anomalyObjects[Random.Range(0, anomalyObjects.Count)]; targetAnomaly.transform.Rotate(0, 90, 0); // Rotate silently when unwatched // Drop a hint in the chat a few seconds later Invoke("DropAnomalyChatHint", 3.0f); } } } void DropAnomalyChatHint() { AddChatMessage("Anonymoose", "Yo... something definitely just moved in the office room."); } // ========================================== // CONCEPT 3: DESKTOP FAKE CHAT SYSTEM // ========================================== IEnumerator SimulateFakeChat() { while (!isGameOver) { yield return new WaitForSeconds(Random.Range(0.5f, 2.0f)); // Fast scrolling chat speed string randomUser = "User_" + Random.Range(100, 999); string randomMessage = chatPool[Random.Range(0, chatPool.Length)]; AddChatMessage(randomUser, randomMessage); } } void AddChatMessage(string user, string message) { chatMessages.Add($"<b>[{user}]</b>: {message}"); // Keep only the last 25 messages so the UI doesn't lag if (chatMessages.Count > 25) chatMessages.RemoveAt(0); chatTextWindow.text = string.Join("\n", chatMessages); // Force scrollbar to move down automatically Canvas.ForceUpdateCanvases(); chatScrollRect.verticalNormalizedPosition = 0f; } // ========================================== // CONCEPT 4: BODYCAM REALISM & JUMPSCARE // ========================================== void HandleMonsterProximity() { if (playerTransform == null || monsterTransform == null) return; float distance = Vector3.Distance(playerTransform.position, monsterTransform.position); // If monster gets relatively close, start glitching the bodycam VHS shader if (distance <= monsterWarningDistance && distance > monsterJumpscareDistance) { float intensity = 1.0f - ((distance - monsterJumpscareDistance) / (monsterWarningDistance - monsterJumpscareDistance)); if (bodycamShaderMaterial != null) bodycamShaderMaterial.SetFloat("_GlitchIntensity", intensity * 0.8f); // Heavy static distort } // JUMPSCARE TRIGGER else if (distance <= monsterJumpscareDistance) { TriggerJumpscare(); } else { if (bodycamShaderMaterial != null) bodycamShaderMaterial.SetFloat("_GlitchIntensity", 0.0f); } } void TriggerJumpscare() { isGameOver = true; if (bodycamShaderMaterial != null) bodycamShaderMaterial.SetFloat("_GlitchIntensity", 1.0f); // Max screen tear static Debug.Log("VIRAL MOMENT: Play ear-rape static sound, force monster animations, show game over screen."); AddChatMessage("LIVE_CHAT", "STREAMER JUST DIED LMAOOOO RIP 💀💀💀"); } // ========================================== // AUXILIARY LOOP CONTROLS // ========================================== void HandlePlayerInputs() { // Example: Press E to complete a chore when interacting if (Input.GetKeyDown(KeyCode.E)) { CompleteChore(); } } void TriggerWinCondition() { isGameOver = true; Debug.Log("Shift over. You survived the night."); AddChatMessage("SYSTEM", "CONNECTION TERMINATED. YOU SURVIVED."); } } 