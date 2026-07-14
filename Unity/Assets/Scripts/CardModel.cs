using System;
using UnityEngine;

[Serializable]
public class CardModel
{
    public int id;
    public string name;
    public int cost;
    public int attack;
    public int defense;
    public string type;
    public string[] tags;
    public int risk;
    public string desc;
}

[Serializable]
public class CardModelList
{
    public CardModel[] items;
}
