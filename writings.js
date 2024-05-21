export const challenge_writing_sample = {
    day: 4,
    questions: [
        {
            id: 1,
            prompt: "退后一步，您在TA之前的写作中看到了哪些非适应性的思维？",
            thoughts: [
                {
                    id: 1,
                    content: "我们家就是这个破德行，从上到下没一个正常人。"
                },
                {
                    id: 2,
                    content: "我妈能不能别老试探来试探去，完全不给我留隐私。"
                }
            ]
        },
        {
            id: 2,
            prompt: "在以上您列出的所有想法里，您看到了哪些类型的非适应性思维？[多选题]",
            thoughts: [
                {
                    id: 1,
                    name: "非黑即白",
                    content: "",
                },
                {
                    id: 2,
                    name: "以偏概全",
                    content:
                        "对应的想法：我们家就是这个破德行，从上到下没一个正常人。",
                },
                {
                    id: 3,
                    name: "灾难化思维",
                    content: "",
                },
                {
                    id: 4,
                    name: "揣摩人心",
                    content: "我妈能不能别老试探来试探去，完全不给我留隐私。",
                },
                {
                    id: 5,
                    name: "过分自责",
                    content: "",
                },
                {
                    id: 6,
                    name: "对号入座",
                    content: "",
                },
                {
                    id: 7,
                    name: "其他",
                    content: "",
                },
                {
                    id: 8,
                    name: "我没有发现自己的非适应性思维。",
                    content: "",
                },
            ],
        },

        {
            id: 3,
            prompt: "接下来，让我们通过问问题来帮助TA寻找更灵活的思维方式。针对您所找到的这些非适应性思维，您会问以下哪几种问题呢？试想一下TA又会怎样回答这些问题呢？您可以结合个人经历使用第一人称回答。[多选题]",
            thoughts: [
                {
                    id: 1, 
                    prompt: "有什么证据可以支持这些想法吗？",
                    content: "除了这件事，倒也没啥。"
                },
                {
                    id: 2, 
                    prompt: "有什么证据可以反驳这些想法吗？",
                    content: "我爸妈从小到大在学习、谈恋爱之类的事情上基本没有过多干涉我的自由。然后我现在工作发展也蛮顺的，算是同学里面混得比较好的了，不能说是废物。"
                },
                {
                    id: 3, 
                    prompt: "这些想法是不是过于极端或者夸张了？",
                    content: "其实除了催婚这件事，我爸妈还算比较正常的吧，平常也不会翻我手机。我之前想的是有点夸张了。"
                },
                {
                    id: 4, 
                    prompt: "这些想法的产生是基于您的感受还是基于事实？",
                    content: ""
                },
                {
                    id: 5, 
                    prompt: "这些想法是不是只关注了事情的一面？",
                    content: ""
                },
                {
                    id: 6, 
                    prompt: "这些想法是否高估了事情发生的概率？",
                    content: ""
                },
                {
                    id: 7, 
                    prompt: "这些想法的信息来源可靠吗？",
                    content: ""
                },
                {
                    id: 8, 
                    prompt: "我没有发现TA的非适应性思维，所以我不需要提问。",
                    content: ""
                },
            ]
        },

        {
            id: 4,
            prompt: "在思考完以上问题之后，您认为TA可以如何更灵活、全面地看待当时的处境？您可以结合个人经历使用第一人称写作。",
            content: "其实说尊重，我妈很多时候也很尊重我的想法。当时我大学一直想学唱歌，虽然这个对普通人来说前景不好，但家里人也支持我学了，送我上学时候我爸妈还哭了。而且我也挺勇敢的，敢选这么个大学专业，证明我不孬。我现在在酒吧驻唱，赚了些钱，家里那个液晶电视就是我买的，虽然摔坏了不过我可以再给家里买新的。至于下一代，要是有下一代，我可能会吸取自己成长中的教训，会比我爸妈更会教育。"
        }
    ],
};


export function addThought(writing, content) {
    const thought = {
        id: writing.questions[0].thoughts.length() + 1,
        content: content
    };
    writing.questions[0].thoughts.push(thought);
}


export const challenge_writing_format = {
    day: 4,
    questions: [
        {
            id: 1,
            prompt: "退后一步，您在TA之前的写作中看到了哪些非适应性的思维？",
            thoughts: []
        },
        {
            id: 2,
            prompt: "在以上您列出的所有想法里，您看到了哪些类型的非适应性思维？[多选题]",
            thoughts: [
                {
                    id: 1,
                    name: "非黑即白",
                    content: "",
                },
                {
                    id: 2,
                    name: "以偏概全",
                    content:
                        "",
                },
                {
                    id: 3,
                    name: "灾难化思维",
                    content: "",
                },
                {
                    id: 4,
                    name: "揣摩人心",
                    content: "",
                },
                {
                    id: 5,
                    name: "过分自责",
                    content: "",
                },
                {
                    id: 6,
                    name: "对号入座",
                    content: "",
                },
                {
                    id: 7,
                    name: "其他",
                    content: "",
                },
                {
                    id: 8,
                    name: "",
                    content: "",
                },
            ],
        },

        {
            id: 3,
            prompt: "接下来，让我们通过问问题来帮助TA寻找更灵活的思维方式。针对您所找到的这些非适应性思维，您会问以下哪几种问题呢？试想一下TA又会怎样回答这些问题呢？您可以结合个人经历使用第一人称回答。[多选题]",
            thoughts: [
                {
                    id: 1, 
                    prompt: "有什么证据可以支持这些想法吗？",
                    content: ""
                },
                {
                    id: 2, 
                    prompt: "有什么证据可以反驳这些想法吗？",
                    content: ""
                },
                {
                    id: 3, 
                    prompt: "这些想法是不是过于极端或者夸张了？",
                    content: ""
                },
                {
                    id: 4, 
                    prompt: "这些想法的产生是基于您的感受还是基于事实？",
                    content: ""
                },
                {
                    id: 5, 
                    prompt: "这些想法是不是只关注了事情的一面？",
                    content: ""
                },
                {
                    id: 6, 
                    prompt: "这些想法是否高估了事情发生的概率？",
                    content: ""
                },
                {
                    id: 7, 
                    prompt: "这些想法的信息来源可靠吗？",
                    content: ""
                },
                {
                    id: 8, 
                    prompt: "我没有发现TA的非适应性思维，所以我不需要提问。",
                    content: ""
                },
            ]
        },

        {
            id: 4,
            prompt: "在思考完以上问题之后，您认为TA可以如何更灵活、全面地看待当时的处境？您可以结合个人经历使用第一人称写作。",
            content: ""
        }
    ],
};

