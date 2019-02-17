using System;
using System.Collections.Generic;
using System.Linq;

namespace trie
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<string> patterns = new List<string>();
            for (int i = 0; i < n; i++)
            {
                string s = Console.ReadLine();
                patterns.Add(s);
            }

            var trie = BuildTrie(patterns);

            for (int i = 0; i < trie.Count(); i++)
            {
                foreach (var edge in trie[i])
                {
                    Console.WriteLine("{0}->{1}:{2}", i, edge.Value.ToString(), edge.Key);
                }
            }
        }

        static List<Dictionary<char, int>> BuildTrie(List<string> patterns)
        {
            var trie = new List<Dictionary<char, int>>();
            // root node
            trie.Add(new Dictionary<char, int>());

            foreach(string pattern in patterns)
            {
                // start with the root node as current node
                var currentNode = trie[0];

                for(int i = 0; i < pattern.Length; i++)
                {
                    int nextNodeIdx;
                    if(currentNode.TryGetValue(pattern[i],out nextNodeIdx) == false)
                    {
                        trie.Add(new Dictionary<char, int>());
                        nextNodeIdx = trie.Count - 1;
                        currentNode.Add(pattern[i], nextNodeIdx);                        
                    }

                    currentNode = trie[nextNodeIdx];                   
                }
            }

            return trie;
        }
    }
}