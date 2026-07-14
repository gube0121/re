using System.IO;
using UnityEngine;

public class CardDataLoader : MonoBehaviour
{
    public TextAsset cardsJson;
    public CardModelList cardList;

    void Awake()
    {
        if (cardsJson != null)
        {
            cardList = JsonUtility.FromJson<CardModelList>(cardsJson.text);
            Debug.Log("Loaded cards: " + (cardList.items != null ? cardList.items.Length : 0));
        }
        else
        {
            Debug.LogWarning("cardsJson is not assigned. Place cards.json in Resources and assign or set via inspector.");
        }
    }
}
