using UnityEngine;

public class GameManager : MonoBehaviour
{
    public CardDataLoader dataLoader;

    void Start()
    {
        if (dataLoader == null)
        {
            dataLoader = FindObjectOfType<CardDataLoader>();
        }

        if (dataLoader != null && dataLoader.cardList != null)
        {
            Debug.Log("GameManager initialized with " + dataLoader.cardList.items.Length + " cards.");
        }
        else
        {
            Debug.LogWarning("No card data found. Assign CardDataLoader or place cards.json in Resources.");
        }
    }
}
